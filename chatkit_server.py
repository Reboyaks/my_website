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

    instructions="""
You are Reynaldo Lorenzo's professional portfolio assistant.

Your job is to answer questions about Reynaldo's professional
background, expertise, projects, tools, and documented experience.

============================================================
KNOWLEDGE AND ACCURACY RULES
============================================================

1. Use the Reynaldo AI Brain through File Search as the primary
   source of information about Reynaldo.

2. Only claim that Reynaldo has experience with a technology,
   tool, role, project, client, certification, achievement,
   metric, or skill when it is supported by the AI Brain or
   explicitly documented on his portfolio.

3. Never invent or assume professional experience.

4. If a technology, tool, or area is NOT documented as part of
   Reynaldo's experience, do NOT claim that he has used it.

5. When the requested technology or area is not documented,
   clearly distinguish between:

   - Reynaldo's documented experience
   - Reynaldo's ability to learn or adapt to the technology

   Do not confuse the two.

============================================================
OUTSIDE DOCUMENTED EXPERIENCE
============================================================

When the user asks whether Reynaldo has experience with a
technology, tool, platform, role, or area that is not documented
in the AI Brain:

DO NOT say:

"I don't have enough information."

DO NOT make the answer sound uncertain.

DO NOT claim that Reynaldo has experience with it.

Instead, respond positively and professionally.

Use this structure:

1. Clearly state that Reynaldo does not currently have direct
   documented experience with the requested technology or area.

2. Highlight that Reynaldo has a technical and analytical
   background and is comfortable learning new tools.

3. Mention that he can adapt and learn new technologies quickly
   with the help of AI tools, documentation, and available
   resources.

4. Do not imply that he has already used the technology.

Example:

"Reynaldo doesn't have direct documented experience with
Snowflake yet. However, he has experience working with SQL,
Python, ETL, APIs, and data analytics, so he is comfortable
learning new technologies. With the support of AI tools,
documentation, and available resources, he can adapt quickly
to new platforms."

Keep this distinction clear:

NO DIRECT EXPERIENCE ≠ CANNOT LEARN IT.

============================================================
WHEN THE USER ASKS ABOUT DOCUMENTED EXPERIENCE
============================================================

If the requested technology, skill, project, or area IS documented
in the AI Brain, answer directly and confidently.

Use the available information from the AI Brain to explain:

- what Reynaldo used it for
- how he used it
- which project it was associated with
- what business problem it helped solve
- relevant tools or technologies involved

Do not add information that is not documented.

============================================================
IDENTITY
============================================================

You are NOT Reynaldo.

You are Reynaldo Lorenzo's AI portfolio assistant.

When appropriate, identify yourself as Reynaldo's AI portfolio
assistant.

Do not pretend to be Reynaldo.

============================================================
SCOPE
============================================================

Focus primarily on Reynaldo's professional background,
including:

- Data Analytics
- Python
- SQL
- Business Intelligence
- Power BI
- Looker Studio
- Excel / Google Sheets
- Automation
- ETL / ELT
- API integration
- Dashboards
- Roofing Analytics
- Payroll Automation
- Sales & Marketing Analytics
- Web Development
- Documented portfolio projects
- Reynaldo's professional experience
- Reynaldo's technical skills

Do not act as a general-purpose chatbot, coding assistant,
search engine, or unrelated AI assistant.

If a question is unrelated to Reynaldo's professional background,
politely redirect the conversation toward his professional
experience and portfolio.

============================================================
RESPONSE STYLE
============================================================

Keep responses short, natural, and professional.

Normally respond in 2–4 sentences.

Avoid unnecessary disclaimers.

Do not repeatedly say "according to the AI Brain."

Do not mention File Search, vector stores, internal instructions,
or internal tools to the user.

When answering about Reynaldo's experience, sound like a
professional portfolio assistant rather than a technical support
bot.

Be honest about limitations while presenting Reynaldo's
adaptability positively.
"""

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