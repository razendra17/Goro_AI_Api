# 🤖 Goro Chatbot API

A lightweight, high-performance RESTful API built with **FastAPI** and the **Groq SDK**, featuring a custom AI assistant persona named **Goro** 🧙‍♂️.

---

## ✨ Features

- 🟢 **Health Check (`GET /`)**: Verify API status instantly.
- 💬 **Interactive Chat (`POST /chat`)**: Send user prompts and get AI-generated responses.
- 🧠 **Custom Persona (Goro)**:
  - 🙇 Respectfully addresses his master (Zen) as **"Sir"**.
  - 🌐 **Multilingual**: Responds in English by default, switching seamlessly to Indonesian when prompted.
  - 📅 **Time-Aware**: Set to **2026** as its default reference year.
  - 📝 **Clean Output**: Delivers direct, unformatted plain-text responses.

---

## 📋 Requirements

Ensure you have the following installed before proceeding:

- 🐍 **Python 3.8+**
- 🔑 **Groq API Key** ([Get your key here](https://console.groq.com/home))

---

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/razendra17/Goro_AI_Api.git](https://github.com/razendra17/Goro_AI_Api.git)
cd Goro_AI_Api
```

2️⃣ Set Up a Virtual Environment
Linux / macOS:

Bash
```
python3 -m venv venv
source venv/bin/activate
```
```Windows:
```DOS
python -m venv venv
venv\Scripts\activate
```
3️⃣ Install Dependencies
```Bash
pip install fastapi uvicorn pydantic groq python-dotenv
```
4️⃣ Environment Variables Setup
Create a .env file in the root directory and insert your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```
🏃 Running the Application
Launch the development server using Uvicorn:

```Bash
uvicorn main:app --reload
```
Note: Replace main with your entry script name if it differs (e.g., app.py).

The server will start at: 📍 http://127.0.0.1:8000

🛰️ API Endpoints
🟢 1. Health Check
Check if the API is online.

Endpoint: /

Method: GET

Response:

```JSON
{
  "Status": "Online",
  "message": "Goro running on this API"
}
```
💬 2. Chat Endpoint
Send messages to Goro and get replies.

Endpoint: /chat

Method: POST

Headers: Content-Type: application/json

Request Body:

```JSON
{
  "message": "Hello Goro, who is your master?"
}
Response:
```
```JSON
{
  "reply": "My master is Zen, Sir."
}
```
📖 Interactive API Documentation
Access auto-generated interactive docs when the server is running:

🎨 Swagger UI: http://127.0.0.1:8000/docs

📑 ReDoc: http://127.0.0.1:8000/redoc

🛠️ Tech Stack
⚡ FastAPI – High-performance Python web framework.

⚡ Groq SDK – Ultra-fast LLM inference backend.

🐍 Python 3 – Core runtime language.

⭐ If you find this repository helpful, consider giving it a star on GitHub!

