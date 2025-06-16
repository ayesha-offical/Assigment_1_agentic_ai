import chainlit as cl
import os
from dotenv import load_dotenv
from agen.agent1_openrouter import generate_dua_with_openrouter
from agen.dua_explainer import explain_with_litellm
from prompt_helper import create_dua_prompt

# Load environment variables
load_dotenv()
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")


@cl.on_chat_start
async def start():
    await cl.Message(content="""
🕌 *Welcome to the AI Dua Generator (Dual Agent)*  
🤖 **Agent 1**: I generate a spiritual Islamic dua based on your feelings.  
📘 **Agent 2**: I explain that dua in simple words.  
💬 *Please share your situation or emotion (e.g., "I'm nervous about exams")*
""").send()

@cl.on_message

async def handle_message(message: cl.Message):
    user_input = message.content.strip()

    if not user_input:
        await cl.Message(content="⚠️ Please describe your situation first.").send()
        return

    # Agent 1: Generate Dua
    await cl.Message(content="🤖 Agent 1 (OpenRouter) is generating your dua...").send()

    prompt = create_dua_prompt(user_input)
    dua = generate_dua_with_openrouter(prompt)

    await cl.Message(content=f"🕋 **Generated Dua:**\n\n{dua}").send()

    # Agent 2: Explain Dua
    await cl.Message(content="📘 Agent 2 (LiteLLM) is explaining the dua...").send()

    explanation = explain_with_litellm(dua)

    await cl.Message(content=f"📖 **Explanation:**\n\n{explanation}").send()