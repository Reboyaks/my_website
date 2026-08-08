import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
workflow_id = os.environ["OPENAI_CHATKIT_WORKFLOW_ID"]

app = FastAPI()


class ChatKitSessionRequest(BaseModel):
    user_id: str


class ChatKitSession(BaseModel):
    client_secret: str


@app.get("/")
def health_check():
    return {"status": "ok", "service": "Reynaldo ChatKit backend"}


@app.post("/api/chatkit/session")
def create_chatkit_session(request: ChatKitSessionRequest):

    if not request.user_id:
        raise HTTPException(
            status_code=400,
            detail="user_id is required"
        )

    response = requests.post(
        "https://api.openai.com/v1/chatkit/sessions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "chatkit_beta=v1",
        },
        json={
            "workflow": {
                "id": workflow_id
            },
            "user": request.user_id,
        },
        timeout=30,
    )

    if not response.ok:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text,
        )

    session = ChatKitSession.model_validate(response.json())

    return {
        "client_secret": session.client_secret
    }