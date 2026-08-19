🤖 Goro Chatbot API
Welcome to the Goro Chatbot API! This is a lightweight, high-performance RESTful API built with FastAPI and Groq SDK, featuring a custom AI assistant persona named Goro 🧙‍♂️.

✨ Features
🟢 Health Check (GET /): Easily check if the API server is up and running.

💬 Interactive Chat (POST /chat): Send messages and receive instant responses from Goro.

🧠 Custom Persona (Goro):

🙇 Respectfully addresses his master as "Sir" (Zen).

🌐 Multilingual support: Responds in English by default, but adapts to Indonesian seamlessly.

📅 Time-aware: Uses 2026 as its default base reference year.

📝 Plain-text formatting: Clean, unformatted direct responses.

📋 Requirements
Before getting started, make sure you have:

🐍 Python 3.8+

🔑 Groq API Key ([Get one here](https://console.groq.com/home))

🚀 Getting Started
Follow these steps to set up and run the project locally.

1️⃣ Clone the Repository
Bash
git clone https://github.com/razendra17/Goro_AI_Api.git
cd Goro_AI_Api

🚨 IMPORTANT
make your own .env file on server folder, and put your groq api there

GROQ_API_KEY= ( your api key )



2️⃣ Set Up Virtual Environment
🐧 For Linux Users: Make sure to activate the Python virtual environment located in the venv directory:

Bash
# Create venv
python3 -m venv venv

# Activate venv (Linux/macOS)
source venv/bin/activate
💻 For Windows Users:

DOS
# Create venv
python -m venv venv

# Activate venv
venv\Scripts\activate
3️⃣ Install Dependencies
Bash
pip install fastapi uvicorn pydantic groq python-dotenv
4️⃣ Configure Environment Variables 🔐
Create a .env file in the root directory of your project and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here
🏃 Run the Application
Start the development server using Uvicorn:

Bash
uvicorn main:app --reload
(Replace main with your file name if it differs, e.g., main.py)

The server will start running at: 📍 [http://127.0.0.1:8000](http://127.0.0.1:8000)

🛰️ API Endpoints
🟢 1. Health Check
Check API status.

URL: /

Method: GET

Response Sample:

JSON
{
  "Status": "Online",
  "message": "Goro running on this API"
}
💬 2. Chat with Goro
Send a message prompt to Goro.

URL: /chat

Method: POST

Headers: Content-Type: application/json

Request Body:

JSON
{
  "message": "Hello Goro, who is your master?"
}
Response Sample:

JSON
{
  "reply": "My master is Zen, Sir."
}
📖 Interactive API Docs
FastAPI automatically generates interactive documentation for your API:

🎨 Swagger UI: http://127.0.0.1:8000/docs

📑 ReDoc: http://127.0.0.1:8000/redoc

🛠️ Tech Stack
⚡ FastAPI - Modern, fast web framework for building APIs.

⚡ Groq Cloud SDK - Ultra-fast LLM inference engine.

🐍 Python 3 - Core programming language.

⭐ If you like this project, feel free to give it a star on GitHub! ⭐