from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal
from recommender import generate_response

app = FastAPI(
    title="SHL Conversational Assessment Recommender",
    description="A FastAPI backend that recommends SHL assessments using catalog-grounded conversational AI.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "SHL Conversational Assessment Recommender",
        "status": "running",
        "message": "API is live. Visit /docs to test the endpoints.",
        "health": "/health",
        "docs": "/docs",
        "redoc": "/redoc",
        "chat_endpoint": "/chat"
    }


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


class Recommendation(BaseModel):
    name: str
    url: str
    test_type: str


class ChatResponse(BaseModel):
    reply: str
    recommendations: List[Recommendation]
    end_of_conversation: bool


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return generate_response(request.messages)