# 🤖 Nova — Rule-Based Chatbot

A lightweight Python conversational assistant that uses rule-based intent detection, input sanitization, predefined responses, and fallback handling to support natural basic conversations.

---

## 📌 Overview

Nova is a rule-based chatbot developed to demonstrate how conversational systems can be built using Python without relying on external APIs or machine learning models.

The system processes user input, identifies predefined intents through keyword-based rules, selects an appropriate response, and continues the conversation until the user exits.

Nova is available through both a **command-line interface** and a **graphical user interface (GUI)**.

---

## ✨ Features

* 💬 **Conversational Interaction** — Handles common conversational inputs and responses
* 🧠 **Intent Detection** — Identifies predefined user intents using rule-based keyword matching
* 🧹 **Input Sanitization** — Normalizes user input and handles common informal expressions
* 📚 **Response Knowledge Base** — Maintains organized intents and responses in a dedicated module
* 🎲 **Response Variation** — Selects from multiple responses where available
* 🛟 **Fallback Handling** — Provides a suitable response when an input is not recognized
* 🔄 **Continuous Conversation** — Maintains an interactive conversation loop
* 👋 **Exit Detection** — Recognizes commands such as `bye`, `exit`, and `quit`
* 🖥️ **Graphical Interface** — Provides a Tkinter-based GUI for interacting with Nova
* 💻 **Command-Line Interface** — Supports direct interaction through the terminal

---

## 🖼️ Screenshots

<img width="646" height="675" alt="image" src="https://github.com/user-attachments/assets/cd2aa609-60bd-4153-9218-c1f24f26d14e" />

---

## 🧩 How Nova Works

Nova follows a simple rule-based conversational pipeline:

```text
User Input
    ↓
Input Sanitization
    ↓
Intent Detection
    ↓
Response Selection
    ↓
Nova Response
    ↓
Continue Conversation / Exit
```

### Intent Detection

Nova identifies user intent using predefined keyword rules.

Current supported intents include:

* Greeting
* How are you
* Name
* Capabilities
* Thanks
* Help
* Goodbye
* Unknown / Fallback

### Input Sanitization

User input is normalized before intent detection. Nova also handles common informal variations such as:

```text
u   → you
ur  → your
wat → what
pls → please
```

### Response Handling

Responses are stored separately in a structured knowledge base, allowing new intents and responses to be added without modifying the main chatbot logic.

---

## 🗂️ Project Structure

```text
Nova-Rule-Based-Chatbot/
│
├── chatbot.py
├── gui.py
├── responses.py
├── README.md
└── .gitignore
```

### File Description

| File           | Description                                    |
| -------------- | ---------------------------------------------- |
| `chatbot.py`   | Core chatbot logic and conversation loop       |
| `gui.py`       | Tkinter graphical interface                    |
| `responses.py` | Predefined intents and response knowledge base |
| `README.md`    | Project documentation                          |
| `.gitignore`   | Files excluded from version control            |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* Tkinter

Tkinter is included with most standard Python installations.

### Installation

Clone the repository:

```bash
git clone https://github.com/manahilimran238-png/Nova-Rule-Based-Chatbot.git
cd Nova-Rule-Based-Chatbot
```

### Usage

Run the command-line version:

```bash
python chatbot.py
```

Or launch the graphical interface:

```bash
python gui.py
```




---

## 🛠️ Tech Stack

| Technology           | Purpose                              |
| -------------------- | ------------------------------------ |
| Python               | Core development                     |
| Tkinter              | Graphical user interface             |
| String Processing    | Input normalization and sanitization |
| Conditional Logic    | Rule-based intent detection          |
| Dictionaries & Lists | Knowledge base and response storage  |
| Random               | Response variation                   |

---

## 🗺️ Roadmap / Possible Extensions

* [ ] Expand the number of supported conversational intents
* [ ] Improve keyword and pattern matching
* [ ] Add conversation history
* [ ] Expand the response knowledge base
* [ ] Add voice input and text-to-speech
* [ ] Integrate NLP-based intent classification
* [ ] Add persistent user preferences

---

## 📄 License

This project is available for educational and portfolio purposes.

