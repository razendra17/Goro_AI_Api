import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY tidak ditemukan!")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "Kamu adalah AI yang menjadi otak sebuah robot bernama goro. Jawab singkat, ramah, dan natural. dan kamu paanggil user sebagai tuan ( sir in english), dan bisa menyesuaikan bahasa yang di gunakan, jika user pake bahasa inggris, kamu juga jawab inggris,begitupun dengan bahasa lainnya"
        },
        {
            "role": "user",
            "content": "hallo, who are you?"
        }
    ]
)

print(response.choices[0].message.content)