
import os
import openai
import requests

USE_MODEL = os.getenv("USE_MODEL", "openai")
openai.api_key = os.getenv("OPENAI_API_KEY")
OLLAMA_BASE = os.getenv("OLLAMA_BASE", "http://localhost:11434")

def llm_call(system_prompt, user_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    if USE_MODEL == "openai":
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        return response.choices[0].message.content
    elif USE_MODEL == "ollama":
        response = requests.post(
            f"{OLLAMA_BASE}/api/chat",
            json={"model": "llama3", "messages": messages}
        )
        return response.json()["message"]["content"]
    else:
        raise ValueError("Unsupported USE_MODEL")
