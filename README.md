# 🤖 Nova — Rule-Based AI Assistant

A simple rule-based chatbot built in Python using predefined intents, conditional logic, input sanitization, and a continuous conversation loop.

## 📌 Project Overview

Nova is a command-line rule-based chatbot that responds to predefined user inputs.

The project demonstrates fundamental programming and basic AI concepts including:

* Control flow
* Decision-making logic
* Intent detection
* Input sanitization
* Knowledge bases
* Fallback handling
* Continuous interaction

No external APIs or machine learning models are required.

---

## ✨ Features

* 👋 Greeting detection
* 🤖 Chatbot identity responses
* 💬 Basic conversation handling
* ❓ Help command
* 🙏 Thank-you responses
* 🔄 Continuous conversation loop
* 🧹 Input sanitization
* 🧠 Rule-based intent detection
* 🛟 Fallback response for unknown inputs
* 👋 Clean exit commands
* 🎲 Multiple responses for each intent

---

## 🧠 Logic Skeleton

The chatbot follows the required rule-based architecture:

```text
User Input
    ↓
Continuous Input Loop
    ↓
Input Sanitization
    ↓
Intent Detection
    ↓
Knowledge Base
    ↓
Response
    ↓
Exit Check
    ↓
Continue / Break
```

### 1. Input Loop

The chatbot uses a continuous `while True` loop to keep accepting user input.

```python
while True:
    user_input = input("You: ").lower().strip()
```

### 2. Sanitization

User input is converted to lowercase and unnecessary whitespace is removed.

```python
user_input = input("You: ").lower().strip()
```

The chatbot also normalizes common informal expressions such as:

* `u` → `you`
* `ur` → `your`
* `wat` → `what`
* `pls` → `please`

### 3. Knowledge Base

Responses are stored in a Python dictionary.

The chatbot contains more than the required five intents:

* `greeting`
* `how_are_you`
* `name`
* `capabilities`
* `thanks`
* `help`
* `goodbye`

An additional `unknown` category is used for fallback responses.

### 4. Intent Detection

Predefined rules are used to determine what the user wants.

For example:

```python
if any(word in user_input for word in greeting_words):
    return "greeting"
```

### 5. Fallback

If no predefined rule matches the user's input, the chatbot returns:

```python
return "unknown"
```

This prevents the program from crashing and provides a default response.

### 6. Exit Strategy

The chatbot recognizes commands such as:

* `bye`
* `goodbye`
* `exit`
* `quit`

When a goodbye intent is detected, the loop is stopped using:

```python
if intent == "goodbye":
    break
```

---

## 📁 Project Structure

```text
Nova-Rule-Based-Chatbot/
│
├── chatbot.py       # Main chatbot logic and conversation loop
├── responses.py     # Knowledge base and predefined responses
├── README.md        # Project documentation
└── .gitignore       # Files excluded from Git
```

---

## 🛠️ Technologies Used

* Python 3
* Conditional statements (`if`, `elif`, `else`)
* `while` loop
* Dictionaries
* Lists
* Functions
* String processing
* `random` module

No external packages are required.

---



## 💬 Example Conversation

```text
<img width="646" height="675" alt="image" src="https://github.com/user-attachments/assets/cd2aa609-60bd-4153-9218-c1f24f26d14e" />




---

## 🧪 Testing

The chatbot was tested with different types of inputs.

| Test Input          | Expected Behavior                        |
| ------------------- | ---------------------------------------- |
| `hello`             | Greeting response                        |
| `HELLO`             | Greeting response after sanitization     |
| `how are you`       | How-are-you response                     |
| `what is your name` | Name response                            |
| `what can u do`     | Capability response                      |
| `can u help me`     | Help response                            |
| `thanks`            | Thank-you response                       |
| Unknown text        | Fallback response                        |
| `bye`               | Goodbye response and program termination |

---


