from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_code_with_gpt(code: str, filename: str) -> str:
    prompt = f"""
You are a senior developer. Review the following code and provide feedback:
- Suggest improvements
- Identify any bad practices
- Point out potential bugs

File: {filename}
Code:
\"\"\"
{code}
\"\"\"
"""
    client = Groq(
        api_key = os.getenv("GROQ_API_KEY")
        
    )

    response = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": prompt,
        }
        ],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message["content"]
