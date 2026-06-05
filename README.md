# 🤖 Mini Jarvis - Voice Assistant

A voice-activated personal assistant built in Python that responds to the wake word **Jarvis** and executes voice commands.

## ✨ Features
- Wake word detection — activates on Jarvis
- Opens websites (YouTube, Google, etc.)
- Plays music via music library
- Fetches latest news
- AI-powered responses using Groq LLaMA3

## 🛠️ Tech Stack
- Python
- SpeechRecognition
- Groq API (LLaMA3)
- pyttsx3 / text-to-speech

## ⚙️ Setup

**1. Clone the repo**
git clone https://github.com/Somnath-001/Mini-Jarvis.git
cd Mini-Jarvis

**2. Create virtual environment**
python -m venv .venv
source .venv/bin/activate

**3. Install dependencies**
pip install -r requirements.txt

**4. Add your API key**
cp .env.example .env
# Open .env and paste your Groq API key
# Get free key at: console.groq.com

**5. Run**
python main.py

## 📁 Project Structure
- main.py — core logic and voice command handling
- client.py — Groq AI integration
- musiclibrary.py — music commands
- news.py — news fetching

## 🔑 Environment Variables
GROQ_API_KEY=your_groq_api_key_here
