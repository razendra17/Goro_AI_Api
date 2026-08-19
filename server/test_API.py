from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel

app = FastAPI()

# type data
class ChatRequest(BaseModel):
    message: str

# endpoint
@app.get("/")
def root():
    return {
        "status": "online",
        "message": "AI Robot Server is running!"
    }


@app.post("/chat")
def chat(data: ChatRequest):
    print("Robot:", data.message)

    return {
        "reply": f"Server menerima: {data.message}"
    }