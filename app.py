import streamlit as st
from agen.agent1_openrouter import generate_dua_with_openrouter
from agen.dua_explainer import explain_with_litellm
from prompt_helper import create_dua_prompt

st.set_page_config(page_title="AI Dua Generator (Dual Agent)", layout="centered")
st.title("🤲 AI Dua Generator")
st.markdown("Enter your feelings or situation below. One agent will generate a dua, and another will explain it.")

dua_input = st.text_area("What's on your heart?", placeholder="e.g. I feel anxious about exams", height=150)

if st.button("Generate Dua"):
    if dua_input.strip():
        with st.spinner("Agent 1 thinking (OpenRouter)..."):
            prompt = create_dua_prompt(dua_input)
            dua_text = generate_dua_with_openrouter(prompt)
            st.session_state.generated_dua = dua_text
            st.success("Dua generated successfully!")  # Changed this line
    else:
        st.warning("Please enter a situation or feeling first.")

# Display the generated dua if present

if "generated_dua" in st.session_state:
    st.markdown("---")
    st.subheader("🕋 Generated Dua")
    st.markdown(st.session_state.generated_dua)

# Explain button outside original block
if st.button("🧠 Explain This Dua (Agent 2 - LiteLLM)"):
    with st.spinner("Agent 2 explaining (LiteLLM)..."):
        explanation = explain_with_litellm(st.session_state.generated_dua)
        st.markdown("---")
        st.subheader("📘 Explanation")
        st.markdown(explanation)


# Footer
st.markdown("""
<hr style="margin-top: 3rem; margin-bottom: 0.5rem;">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
<div style='text-align: center; font-size: 14px; color: gray;'>
    Created by Ayesha 🌙 |
    <a href="https://github.com/ayesha-offical" target="_blank" style="color: gray; text-decoration: none;">
        <i class="fab fa-github"></i> GitHub
    </a>
</div>
""", unsafe_allow_html=True)