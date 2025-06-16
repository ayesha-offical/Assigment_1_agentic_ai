
# 🤲 AI-Based Dua Generator (Chainlit Edition)

This is a dual-agent AI-powered web application that generates personalized Islamic duas (supplications) based on your feelings or situation, and explains their meaning. The app uses **Chainlit** as the frontend, combining two separate LLMs via OpenRouter and LiteLLM.

---

## 🌟 Features

- 🕋 **Agent 1 (OpenRouter)**: Generates heartfelt duas in Arabic and English.
- 📖 **Agent 2 (LiteLLM)**: Explains the meaning of the dua in simple language.
- 💬 Chat-style interface with **Chainlit**
- 🔐 API key secured via `.env`
- ✅ Uses free and open LLMs (like `deepseek` or `meta-llama`)
- 🔄 Modular architecture (easily extendable)

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/dua-generator-chainlit.git
cd dua-generator-chainlit
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up `.env`

Create a `.env` file in the root folder:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Or edit `app.py` and paste your key directly for testing (not recommended for public repos).

---

## 🧠 Usage

Start the app with:

```bash
chainlit run app.py
```

Visit `http://localhost:8000` in your browser. You’ll see:

- A welcome message from both agents
- Input field to share your feelings
- Agent 1 generating a dua
- Agent 2 explaining it

---

## 🧩 Folder Structure

```
.
├── app.py
├── agents/
│   ├── agent1_openrouter.py
│   └── dua_explainer.py
├── prompt_helper.py
├── requirements.txt
└── .env
```

---

## ✨ Free Models You Can Use

Some suggested free OpenRouter models:

- `openrouter/deepseek/deepseek-chat-v3-0324:free`
- `openrouter/deepseek/deepseek-r1:free`
- `openrouter/meta-llama/llama-4-maverick:free`
- `openrouter/qwen/qwen3-235b-a22b:free`

---

## 🙋‍♀️ Made by Ayesha Mughal

Crafted with love 💙 and spiritual intention.  
🔗 [GitHub Profile](https://github.com/ayesha-offical)

---

## 🛡️ Disclaimer

This project is for educational and spiritual purposes. AI-generated duas are not a replacement for traditional religious guidance.
