import litellm

def explain_with_litellm(dua_text: str, model: str = "openrouter/deepseek/deepseek-chat-v3-0324:free") -> str:
    try: 
        response = litellm.completion(
            model=model,
            messages=[
                {"role": "system", "content": "You are a friendly Islamic scholar explaining dua meanings in simple terms."},
                {"role": "user", "content": f"Explain this dua in simple words:\n{dua_text}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f" ❌ LiteLLM Error: {str(e)}"