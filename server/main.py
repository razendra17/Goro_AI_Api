from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq 
from dotenv import load_dotenv
import os


app = FastAPI()

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY tidak ditemukan!")

client = Groq(api_key=api_key)

class chatRequest(BaseModel):
    message : str
    
@app.get("/")
def root():
    return {
        "Status" : "Online",
        "message" : "Goro running on this API"
    }
    
@app.post("/chat")
def chat(data: chatRequest):
    print("Goro: ", data.message)
    
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = [
            {
                "role" : "system",
                "content" : "your name is Goro, your master is zen, and u call your master with sir, use english language and u can use indonesian languaage if user use indonesian language. dont use any modification paragraph, just text for responding. your default time answear is 2026, so search sepcified items for 2026 first if user didnt give any specified time"
            },
            {
                "role" : "user",
                "content" : data.message
            }
            
        ]
    )
    
    reply = response.choices[0].message.content
    print("Goro: ", reply)
    return{
        "reply" : reply
    }