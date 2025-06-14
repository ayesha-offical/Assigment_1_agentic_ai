def create_dua_prompt(user_input:str) -> str:
    return f"""
    You are an Islamic assistant. Generate a short Islamic dua in Arabic and English for this situation:

"{user_input}"

Respond in this exact format using Markdown:
**Arabic Dua:** [Arabic text]

**English Translation:** [English translation]

**Short Explanation:** [One-line explanation of when this dua is used]

Keep it short, authentic, and spiritually.
"""