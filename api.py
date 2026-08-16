from fastapi import FastAPI
from pydantic import BaseModel

from agent import run_agent

app = FastAPI(title="Agentic AI API")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    answer = run_agent(request.message)
    return ChatResponse(response=answer)


def start() -> None:
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
