import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
def generate_dua_with_openrouter(prompt: str, model: str = "deepseek/deepseek-r1:free") -> str:
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": "You are an Islamic assistant generating heartfelt duas."},
                    {"role": "user", "content": prompt}
                ]
            }
        )

        result = response.json()

        # 🔍 Debugging help — print error if it exists
        if "choices" not in result:
            return f"❌ OpenRouter Error:\n{result}"

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ OpenRouter Error: {str(e)}"
