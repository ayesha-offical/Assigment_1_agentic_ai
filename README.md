# 🤲 AI-Based Dua Generator (Dual Agent)

This is a dual-agent AI web app built with **Streamlit**, where one AI agent generates personalized Islamic duas, and the second AI agent explains them in simple language — using two different LLM providers (OpenRouter and LiteLLM).

---

## 🌟 Features

- ✨ **Agent 1 (OpenRouter)**:  
  Generates a spiritually uplifting dua in Arabic and English based on the user's emotional input.

- 📘 **Agent 2 (LiteLLM)**:  
  Explains the meaning of the generated dua using a separate model.

- 💬 Simple UI built with **Streamlit**

- ✅ Uses **Open-source & free models** (like DeepSeek via OpenRouter)

- 📂 Modular code with session-based logic for smooth interaction

---

## 🚀 How to Run the Project

### 1. Clone the repo:

```bash
git clone https://github.com/yourusername/ai-dua-generator.git
cd ai-dua-generator
```

### 2. Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scriptsctivate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> 🔑 Get a free API key from: https://openrouter.ai/

---

## 🧠 Technologies Used

- Python 3.x
- Streamlit
- OpenRouter API
- LiteLLM
- dotenv

---

## 📁 Folder Structure

```
├── app.py
├── prompt_helper.py
├── agents/
│   ├── agent1_openrouter.py
│   └── dua_explainer.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🎯 Use Cases

- Spiritual reflection tools
- Personalized AI Islamic assistant
- AI for emotional + religious well-being

---

## 🙋‍♀️ Created By

**Ayesha Mughal**  
🔗 [GitHub](https://github.com/ayesha-offical)  
🌙 Powered with love and Imaan

---
## Here you can test:

Link 
## 🛡️ Disclaimer

This is a learning and research-based project. The generated content is AI-based and should be cross-checked with authentic Islamic scholars for accuracy and religious correctness.
