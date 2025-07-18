

# 🧠 Python AI Chat Assistant

This is a **Python-based AI assistant. It can chat with you, answer questions, and remember the flow of the conversation. You can run it directly in Python IDLE or any terminal.

---

## 🚀 Features

✅ Chat with a GPT-powered AI assistant.
✅ Remembers the conversation flow for more natural replies.
✅ Handles multi-turn dialogue.
✅ Simple text-based interface.

---

## 🛠 Requirements

* Python 3.8 or higher
* Libraries:

  * `openai`
  * (Optional for GUI: `tkinter`)

Install dependencies:

```bash
pip install openai
```

---

## 📥 Setup Instructions

1. Clone this repository or download the files.

```bash
git clone https://github.com/yourusername/ai-assistant.git
cd ai-assistant
```

2. Install Python dependencies:

```bash
pip install openai
```

3. Get your OpenAI API key:

   * Sign up at [OpenAI](https://platform.openai.com/).
   * Go to **API Keys**, create a new key, and copy it.

4. Open `chatbot.py` and paste your API key:

```python
openai.api_key = "YOUR_API_KEY_HERE"
```

---

## 🏃‍♂️ How to Run

1. Open **Python IDLE** or your terminal.
2. Run the assistant:

```bash
python chatbot.py
```

3. Start chatting! Type your message and press Enter.
4. Type `bye` to exit.

---

## 🖥 Example

```
You: Hello!
Bot: Hi there! How can I assist you today?

You: What is Python?
Bot: Python is a high-level, interpreted programming language known for its simplicity and versatility.

You: bye
Bot: Goodbye! 👋
```

---

## 📌 Next Steps

* Add a **GUI** interface (Tkinter).
* Enable **voice input and output**.
* Integrate with external APIs (weather, Wikipedia, etc).
