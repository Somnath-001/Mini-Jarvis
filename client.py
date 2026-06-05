import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_APoI_KEY"))

def ai_process(user_input):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant. Keep responses short and helpful."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None
    )

    response = ""
    for chunk in completion:
        content = chunk.choices[0].delta.content or ""
        print(content, end="", flush=True)
        response += content
    return response