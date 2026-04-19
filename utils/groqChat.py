import os
from dotenv import load_dotenv

from groq import Groq

load_dotenv()
GROQ_KEY = os.getenv("GROQ_KEY")

groq = Groq(api_key=GROQ_KEY)

def groqChat(text, role="user"):
    chatCompletion = groq.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Siz foydali yordamchisiz. FAQAT <b>, <i>, <pre><code> formatlarini ishlating. Boshqa teglarni ishlatmang."
            },
            {
                "role": role,
                "content": text
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    return chatCompletion.choices[0].message.content