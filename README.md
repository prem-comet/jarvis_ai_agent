# jarvis_ai_agent
This is AI agent which speaks as well as chat


🤖 Jarvis AI Agent
A voice-powered AI assistant built using Python and the OpenAI API, capable of chatting and speaking responses — inspired by Iron Man's Jarvis.

🧠 Features
💬 Chat with the AI using text or voice

🔊 Text-to-speech (TTS) capability to make the AI speak

🧑‍💻 Powered by OpenAI's GPT API (ChatGPT)

🖥️ Simple and interactive command-line interface

🛠️ Extensible architecture for adding more commands and functionality

🧰 Technologies Used
Python 3.x

OpenAI GPT API

pyttsx3 / gTTS (for Text-to-Speech)

SpeechRecognition (for speech input)

plyer import notification  ( for notification )

import pyautogui( for windows functionality or windows interaction )

import pywhatkit as pwk ( for what's_app interaction )

import webbrowser  ( for webbrowser interaction )

import smtplib , ssl ( for email purpose )

Other standard Python libraries (like wikipedia , time, etc.)




// Flow Chart of this project is given below :-

jarvis-ai-agent/
│
├── main.py                # Entry point of the application
├── openai_request.py        # Handles ai based model
├── PyWhatKit_DB.py         # Manages whatsapp interactions
├── speech.py       # Handles Speech functionality
|__user_config_py   # To store sensitive information or API_KEY

