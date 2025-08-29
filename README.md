# Async OpenAI Chatbot

A simple terminal-based chatbot powered by OpenAI’s `gpt-3.5-turbo` model.  
The bot runs asynchronously using `asyncio` and reads your API key from a `.env` file.

---

## 🚀 Features
- Interactive chat in the terminal
- Asynchronous API calls with `AsyncOpenAI`
- Loads API key securely from `.env`
- Gracefully exits when user types `quit`, `exit`, or `bye`

---

## 📦 Requirements
- Python 3.9+
- Dependencies listed in `requirements.txt`:
  - `openai`
  - `python-dotenv`

---

## ⚙️ Setup

1. **Clone this repository (or copy the script):**
   ```bash
   git clone https://github.com/bibekgyawali11/openai-chatbot.git
   cd openai-chatbot

2. Install dependencies
pip install -r requirements.txt

3. Create a .env file in the project directory and add your OpenAI API key:
API_KEY=sk-your-openai-api-key
Go to [OpenAI API Keys page](https://platform.openai.com/account/api-keys) for creating the keys

4. Run the chatbot
python chat_bot.py
