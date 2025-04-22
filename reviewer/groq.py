import os
import requests
from dotenv import *

GROQ_API_KEY = get_key("key.env", "GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile" 

def analyze_code_with_groq(code: str, filename: str) -> str:
    """
    Analiza el código proporcionado utilizando la API de Groq y devuelve un análisis detallado.

    @param code: El código fuente a analizar como string.
    @param filename: El nombre del archivo que contiene el código.
    @return: Un string con el análisis generado por la API de Groq.
    """
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY in environment variables.")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an expert code reviewer. Please analyze the following file and provide:
- Constructive suggestions
- Any bugs or performance issues
- Best practices violations
- Style improvements

Filename: {filename}
Code:
\"\"\"
{code}
\"\"\"
"""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code != 200:
        print("Groq API error:", response.text)
        raise Exception("Failed to get response from Groq API.")

    return response.json()["choices"][0]["message"]["content"]
