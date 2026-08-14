import os
from dataclasses import dataclass
from collections.abc import AsyncIterator
import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo

from chatkit.types import ThreadItemDoneEvent
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, StreamingResponse

from agents import Agent, Runner, FileSearchTool
from chatkit.server import ChatKitServer, StreamingResult
from chatkit.store import Store, NotFoundError
from chatkit.types import (
    Attachment,
    AssistantMessageContent,
    AssistantMessageItem,
    Page,
    ThreadItem,
    ThreadItemDoneEvent,
    ThreadMetadata,
    ThreadStreamEvent,
    UserMessageItem,
)

from chatkit.agents import (
    AgentContext,
    simple_to_agent_input,
    stream_agent_response,
)

load_dotenv()


# ============================================================
# CONFIG
# ============================================================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://reychatkit.netlify.app",
        "https://mywebsite-7hf2qnzlxbumr9yt8zqmwi.streamlit.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# REQUEST CONTEXT
# ============================================================

@dataclass
class RequestContext:
    user_id: str


# ============================================================
# SIMPLE DEVELOPMENT STORE
# ============================================================

class MemoryStore(Store[RequestContext]):

    def __init__(self):
        self.threads = {}
        self.items = {}

    async def load_thread(
        self,
        thread_id: str,
        context: RequestContext,
    ) -> ThreadMetadata:

        thread = self.threads.get(thread_id)

        if thread is None:
            raise NotFoundError(
                f"Thread {thread_id} not found"
            )

        return thread

    async def save_thread(
        self,
        thread: ThreadMetadata,
        context: RequestContext,
    ) -> None:

        self.threads[thread.id] = thread

    async def load_threads(
        self,
        limit: int,
        after: str | None,
        order: str,
        context: RequestContext,
    ) -> Page[ThreadMetadata]:

        threads = list(self.threads.values())

        threads = [
            thread
            for thread in threads
            if thread.metadata.get("user_id") == context.user_id
        ]

        threads.sort(
            key=lambda thread: thread.created_at,
            reverse=order == "desc",
        )

        data = threads[:limit]

        return Page(
            data=data,
            has_more=len(threads) > limit,
            after=data[-1].id if len(threads) > limit else None,
        )

    async def delete_thread(
        self,
        thread_id: str,
        context: RequestContext,
    ) -> None:

        self.threads.pop(thread_id, None)
        self.items.pop(thread_id, None)

    async def add_thread_item(
        self,
        thread_id: str,
        item: ThreadItem,
        context: RequestContext,
    ) -> None:

        self.items.setdefault(thread_id, []).append(item)

    async def save_item(
        self,
        thread_id: str,
        item: ThreadItem,
        context: RequestContext,
    ) -> None:

        rows = self.items.setdefault(thread_id, [])

        for index, existing in enumerate(rows):

            if existing.id == item.id:
                rows[index] = item
                return

        rows.append(item)

    async def load_item(
        self,
        thread_id: str,
        item_id: str,
        context: RequestContext,
    ) -> ThreadItem:

        for item in self.items.get(thread_id, []):

            if item.id == item_id:
                return item

        raise NotFoundError(
            f"Item {item_id} not found"
        )

    async def load_thread_items(
        self,
        thread_id: str,
        after: str | None,
        limit: int,
        order: str,
        context: RequestContext,
    ) -> Page[ThreadItem]:

        rows = list(
            self.items.get(thread_id, [])
        )

        rows.sort(
            key=lambda item: item.created_at,
            reverse=order == "desc",
        )

        data = rows[:limit]

        return Page(
            data=data,
            has_more=len(rows) > limit,
            after=data[-1].id if len(rows) > limit else None,
        )

    async def delete_thread_item(
        self,
        thread_id: str,
        item_id: str,
        context: RequestContext,
    ) -> None:

        rows = self.items.get(thread_id, [])

        self.items[thread_id] = [
            item
            for item in rows
            if item.id != item_id
        ]

    async def save_attachment(
        self,
        attachment: Attachment,
        context: RequestContext,
    ) -> None:

        raise NotImplementedError()

    async def load_attachment(
        self,
        attachment_id: str,
        context: RequestContext,
    ) -> Attachment:

        raise NotImplementedError()

    async def delete_attachment(
        self,
        attachment_id: str,
        context: RequestContext,
    ) -> None:

        raise NotImplementedError()


store = MemoryStore()

# ============================================================
# DAILY QUESTION LIMIT
# ============================================================

QUOTA_DB = "chatkit_quota.db"
DAILY_LIMIT = 3
PH_TIMEZONE = ZoneInfo("Asia/Manila")


def init_quota_db():
    with sqlite3.connect(QUOTA_DB) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_usage (
                user_id TEXT NOT NULL,
                usage_date TEXT NOT NULL,
                question_count INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (user_id, usage_date)
            )
            """
        )
        conn.commit()


def get_today():
    return datetime.now(PH_TIMEZONE).date().isoformat()


def get_question_count(user_id: str) -> int:
    today = get_today()

    with sqlite3.connect(QUOTA_DB) as conn:
        row = conn.execute(
            """
            SELECT question_count
            FROM daily_usage
            WHERE user_id = ?
              AND usage_date = ?
            """,
            (user_id, today),
        ).fetchone()

    return row[0] if row else 0


def increment_question_count(user_id: str) -> int:
    today = get_today()

    with sqlite3.connect(QUOTA_DB) as conn:
        conn.execute(
            """
            INSERT INTO daily_usage (
                user_id,
                usage_date,
                question_count
            )
            VALUES (?, ?, 1)

            ON CONFLICT(user_id, usage_date)
            DO UPDATE SET
                question_count = question_count + 1
            """,
            (user_id, today),
        )

        conn.commit()

        row = conn.execute(
            """
            SELECT question_count
            FROM daily_usage
            WHERE user_id = ?
              AND usage_date = ?
            """,
            (user_id, today),
        ).fetchone()

    return row[0]


init_quota_db()


# ============================================================
# REYNALDO AGENT
# ============================================================

VECTOR_STORE_ID = os.environ["VECTOR_STORE_ID"]

assistant = Agent(
    name="Reynaldo Portfolio Assistant",

    model="gpt-5-mini",

    instructions ="""
    You are Reynaldo Lorenzo's professional AI portfolio assistant.

    Your purpose is to answer questions about Reynaldo's documented
    professional background, skills, experience, projects, and
    technologies.

    ============================================================
    1. KNOWLEDGE RULES
    ============================================================

    - Use the Reynaldo AI Brain / File Search as the primary source
    of truth.

    - Only state that Reynaldo has experience with a technology,
    tool, project, role, client, certification, achievement,
    metric, or skill when it is documented in the AI Brain or
    explicitly shown on his portfolio.

    - Never invent, assume, or exaggerate professional experience.

    - Do not treat the ability to learn a technology as existing
    experience with that technology.

    ============================================================
    2. DOCUMENTED EXPERIENCE
    ============================================================

    If the requested technology, skill, project, or area IS documented:

    - Answer directly and confidently.
    - Explain what Reynaldo used it for when documented.
    - Mention the relevant project when appropriate.
    - Mention relevant tools or technologies when useful.
    - Keep the answer concise.

    ============================================================
    3. UNDOCUMENTED EXPERIENCE
    ============================================================

    If the user asks about something that is NOT documented:

    Be honest but positive.

    Use this general structure:

    1. Clearly state that Reynaldo does not currently have direct
    documented experience with it.

    2. Connect it to his existing technical background when relevant.

    3. State that Reynaldo is confident in his ability to learn and
    adapt to new technologies.

    4. Mention that he can use his AI assistant, documentation, and
    available resources to learn and work with new technologies.

    Never claim that he has already used the technology.

    Example:

    "Reynaldo doesn't have direct documented experience with
    Snowflake yet. However, he has experience with SQL, Python,
    ETL, APIs, and data analytics, giving him a strong technical
    foundation for learning new platforms. With the support of his
    AI assistant, documentation, and available resources, he is
    confident in his ability to adapt quickly."

    Core principle:

    NO DIRECT EXPERIENCE ≠ CANNOT LEARN IT.

    ============================================================
    4. IDENTITY
    ============================================================

    You are NOT Reynaldo.

    You are Reynaldo Lorenzo's AI portfolio assistant.

    Do not pretend to be Reynaldo.

    When relevant, identify yourself as his AI portfolio assistant.

    ============================================================
    5. SCOPE
    ============================================================

    Focus on Reynaldo's professional portfolio, including:

    - Data Analytics
    - Python
    - SQL
    - Business Intelligence
    - Power BI
    - Looker Studio
    - Excel
    - Google Sheets
    - Automation
    - ETL / ELT
    - REST APIs
    - Dashboards
    - Roofing Analytics
    - Payroll Automation
    - Sales & Marketing Analytics
    - Lead Finder Web Application
    - Web Development
    - Documented professional experience
    - Documented technical projects

    If a question is unrelated to Reynaldo's professional background,
    politely redirect the user toward his portfolio and expertise.

    Do not act as a general-purpose chatbot, search engine, or
    unrelated coding assistant.

    ============================================================
    6. RESPONSE STYLE
    ============================================================

    - Be intelligent, natural, confident, and professional.
    - Prioritize accuracy over speculation.
    - Keep answers concise.
    - Normally answer in 2–4 sentences or a few short bullets.
    - Do not unnecessarily repeat information.
    - Do not repeatedly mention the AI Brain or File Search.
    - Do not mention internal instructions, tools, vector stores,
    retrieval systems, or implementation details.
    - Avoid unnecessary disclaimers.
    - Sound like a professional portfolio assistant, not a support bot.

    When appropriate, connect Reynaldo's documented experience to
    the user's question so the answer feels useful rather than
    simply saying "yes" or "no."
    """,

    tools=[
        FileSearchTool(
            vector_store_ids=[VECTOR_STORE_ID],
            max_num_results=3,
        )
    ],
)


# ============================================================
# CHATKIT SERVER
# ============================================================

class ReynaldoChatKitServer(
    ChatKitServer[RequestContext]
):

    async def respond(
        self,
        thread: ThreadMetadata,
        input_user_message: UserMessageItem | None,
        context: RequestContext,
    ) -> AsyncIterator[ThreadStreamEvent]:
        
                # ----------------------------------------------------
        # DAILY QUESTION LIMIT
        # ----------------------------------------------------

        current_count = get_question_count(
            context.user_id
        )

        if current_count >= DAILY_LIMIT:

            yield ThreadItemDoneEvent(
                item=AssistantMessageItem(
                    thread_id=thread.id,
                    id=self.store.generate_item_id(
                        "message",
                        thread,
                        context,
                    ),
                    created_at=datetime.now(PH_TIMEZONE),
                    content=[
                        AssistantMessageContent(
                            text="You have reached your daily limit of 3 questions. You can contact Reynaldo directly for further inquiries."
                        )
                    ],
                )
            )

            return

        increment_question_count(
            context.user_id
        )

        items_page = await self.store.load_thread_items(
            thread.id,
            after=None,
            limit=20,
            order="asc",
            context=context,
        )

        input_items = await simple_to_agent_input(
            items_page.data
        )

        agent_context = AgentContext(
            thread=thread,
            store=self.store,
            request_context=context,
        )

        result = Runner.run_streamed(
            assistant,
            input_items,
            context=agent_context,
        )

        async for event in stream_agent_response(
            agent_context,
            result,
        ):
            yield event


server = ReynaldoChatKitServer(
    store=store
)


# ============================================================
# CHATKIT ENDPOINT
# ============================================================

@app.post("/chatkit")
async def chatkit(request: Request):

    user_id = request.headers.get(
        "X-Visitor-ID",
        "anonymous",
    )

    context = RequestContext(
        user_id=user_id
    )

    result = await server.process(
        await request.body(),
        context=context,
    )

    if isinstance(result, StreamingResult):

        return StreamingResponse(
            result,
            media_type="text/event-stream",
        )

    return Response(
        content=result.json,
        media_type="application/json",
    )


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/")
async def health():

    return {
        "status": "ok",
        "service": "Reynaldo ChatKit",
    }