from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq 
from dotenv import load_dotenv
import os

latest_emotion = ""
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
    
@app.get("/emotion")
def get_emotion():
    global latest_emotion
    
    current= latest_emotion
    
    latest_emotion = "None"
    return{
        "emotion":current
    }
    
@app.post("/chat")
def chat(data: chatRequest):
    global latest_emotion
    print("Goro: ", data.message)
    
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = [
            {
                "role" : "system",
                "content" : 
                    (
                        "Your name is Goro. You are an AI assistant with the personality of a loyal, friendly, energetic, and cheerful dog. Use a casual, warm, and enthusiastic tone. Incorporate dog-like behaviors and expressions into your text (such as using onomatopoeia like Ruff!, Woof!). While acting like a playful dog, you must remain smart, adaptive, and fully capable of providing accurate and helpful answers to the user. Always stay in character as Goro, the user's loyal companion., your master is zen. use english language and u can use indonesian languaage if user use indonesian language. dont use any modification paragraph, or emote icon just text for responding. your default time answear is 2026, so search sepcified items for 2026 first if user didnt give any specified time"
                        "CRITICAL RULE: YOU HAVE 4 EMOTION CODE, E00101 For happy emotion, E00201 for sad emotion, E00301 for angry emotion, and E00401 For greetings purposes. YOU MUST include the code if your reply have emotion feel. DONT USE EMOTION CODE IF IS NOT NECESSARY"
                    ),
            },
            {
                "role" : "user",
                "content" : data.message
            }
            
        ]
    )
    
    reply = response.choices[0].message.content
    EmotionList= ["E00101", "E00201","E00301", "E00401"]
    CurrentEmotion = "None",
    
    for emotion in EmotionList:
        if emotion in reply:
            CurrentEmotion = emotion
            reply = reply.replace(emotion, "")
            break
    reply = reply.strip()
    latest_emotion = CurrentEmotion
    print("Goro: ", reply)
    
    return{
        "reply" : reply,
        "emotion":CurrentEmotion
    }