import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

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
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message["content"]
