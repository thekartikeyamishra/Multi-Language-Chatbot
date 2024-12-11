# Multi-Language-Chatbot
For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!
The **Multi-Language Chatbot** is a Python-based chatbot that allows users to communicate in multiple languages (e.g., English, Hindi, and Spanish). The chatbot uses pre-defined responses for common queries and a translation API to handle multi-language input.

### README File

```markdown
## Overview

The **Multi-Language Chatbot** is a Python-based chatbot that allows users to communicate in multiple languages (e.g., English, Hindi, and Spanish). The chatbot uses pre-defined responses for common queries and a translation API to handle multi-language input.

This project is designed to provide a simple chatbot experience with multi-language support via a clean and user-friendly GUI built with **Tkinter**.

---

## Features

- **Multi-Language Support**:
  - Communicate in English (`en`), Hindi (`hi`), and Spanish (`es`).
- **Pre-Defined Responses**:
  - Chatbot responds to common queries like greetings, help, and goodbyes.
- **Translation API**:
  - Automatically translates user queries to English for processing and then back to the user’s chosen language.
- **Simple GUI**:
  - A Tkinter-based graphical interface for sending and receiving messages.

---

## Folder Structure

Below is the folder structure of the project:

```bash
MultiLanguageChatbot/
├── data/
│   ├── responses.json           # Pre-defined responses for different languages
├── gui/
│   ├── __init__.py              # Initializes the GUI module
│   ├── chatbot_gui.py           # GUI implementation using Tkinter
├── utils/
│   ├── __init__.py              # Initializes the utils module
│   ├── translation_api.py       # Logic for translating text using Google Translate API
│   ├── response_logic.py        # Logic to fetch responses based on user queries
├── main.py                      # Entry point to run the chatbot
├── requirements.txt             # Dependencies required for the project
├── README.md                    # Documentation for the project
```

---

## Installation and Setup

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8+**
- **pip**: Python's package manager.

---

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/thekartikeyamishra/MultiLanguageChatbot.git
   cd MultiLanguageChatbot
   ```

2. **Set Up Virtual Environment**

   Create and activate a virtual environment to isolate dependencies:
   - On **Windows**:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**

   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   Start the application by running the `main.py` script:
   ```bash
   python main.py
   ```

---

## How to Use

1. Launch the chatbot by running `main.py`.
2. Select your preferred language from the dropdown menu (English, Hindi, or Spanish).
3. Type your message in the input field and click the **"Send"** button.
4. The chatbot will process your query and respond in the selected language.
5. Continue the conversation or change the language anytime.

---

## Example Interaction

**Example in English**:
```
You: Hello
Bot: Hello! How can I assist you?
You: Goodbye
Bot: Goodbye! Have a great day!
```

**Example in Hindi**:
```
You: नमस्ते
Bot: नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?
You: अलविदा
Bot: अलविदा! आपका दिन शुभ हो!
```

**Example in Spanish**:
```
You: Hola
Bot: ¡Hola! ¿Cómo puedo ayudarte?
You: Adiós
Bot: ¡Adiós! ¡Que tengas un gran día!
```

---

## Dependencies

The project uses the following Python libraries:
- **googletrans**: For translating text between languages.
- **tkinter**: For building the graphical user interface.
- **json**: For managing pre-defined responses.

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

---

## Acknowledgments

- **Google Translate API**: Used for multi-language translation.
- **Python**: The programming language used to build this chatbot.
- **Tkinter**: For the graphical user interface.

```

---
Here's how the folder structure will look:

MultiLanguageChatbot/
├── data/
│   ├── responses.json           # Pre-defined responses for different languages
│       └── # Example JSON structure
├── gui/
│   ├── __init__.py              # Initializes the GUI module
│   ├── chatbot_gui.py           # GUI implementation using Tkinter
├── utils/
│   ├── __init__.py              # Initializes the utils module
│   ├── translation_api.py       # Logic for translating text using Google Translate API
│   ├── response_logic.py        # Logic to fetch responses based on user queries
├── main.py                      # Entry point to run the chatbot
├── requirements.txt             # Dependencies required for the project
├── README.md                    # Documentation for the project

