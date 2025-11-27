from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Demo FastAPI App")


class EchoRequest(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"status": "ok", "message": "FastAPI demo is running"}


@app.post("/echo")
def echo(request: EchoRequest):
    # Simple demo endpoint that echoes the provided payload
    return {"echo": request.message}

