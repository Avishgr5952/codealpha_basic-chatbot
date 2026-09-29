# TASK 4: Basic Chatbot

A simple, beginner-friendly console-based chatbot implemented in pure Python.

---

## Objective

The objective of this project is to build a rule-based chatbot using fundamental Python programming constructs. The chatbot interacts with users in the terminal, processes their text input, and provides predefined responses based on specified rules until instructed to exit.

---

## Features

- **Interactive Console Interface**: Communicates via standard terminal input and output (`input()` and `print()`).
- **Continuous Conversation**: Runs continuously in a `while` loop until the user types `bye`.
- **Predefined Rule-Based Responses**: Supports standard greetings, inquiries, help messages, and fallback handling.
- **Input Sanitization**:
  - **Case-Insensitive**: Converts user input to lowercase so inputs like `HELLO`, `Hello`, and `hello` match identically.
  - **Whitespace Trimming**: Strips unnecessary leading and trailing whitespace.
- **Fallback Response**: Gracefully handles unknown commands or unrecognized inputs with an informative message.
- **No External Dependencies**: Operates entirely with Python's built-in capabilities without requiring any third-party libraries or internet connectivity.

---

## Technologies Used

- **Language**: Python 3 (standard installation)
- **Dependencies**: None (pure Python standard library)

---

## How the Chatbot Works

1. **Startup**: When executed, the program prints a welcome banner and instructions.
2. **User Input**: The chatbot waits for user input using Python's `input()` function.
3. **Data Sanitization**: The string is stripped of leading and trailing spaces using `.strip()` and converted to lowercase using `.lower()`.
4. **Rule Matching (`if/elif/else`)**: The cleaned input is passed to the `get_response()` function, which matches the text against known rules:
   - `"hello"` &rarr; `"Hi! How can I help you?"`
   - `"hi"` &rarr; `"Hello! Nice to meet you."`
   - `"how are you"` &rarr; `"I'm doing great! How are you?"`
   - `"what is your name"` &rarr; `"I'm a simple Python chatbot."`
   - `"help"` &rarr; Displays list of available commands
   - `"bye"` &rarr; `"Goodbye! Have a great day!"`
   - Any other input &rarr; `"Sorry, I don't understand that."`
5. **Output**: The response is displayed on the console.
6. **Exit Condition**: If the sanitized input is `"bye"`, the loop terminates and the program exits.

---

## Python Concepts Used

- **Input/Output (`input()`, `print()`)**: Capturing user entries and printing responses to the console.
- **Variables**: Storing user input strings and responses.
- **String Methods (`strip()`, `lower()`)**: Normalizing user input for robust matching.
- **Functions (`def`)**: Modularizing code into clean, reusable functions (`get_response()` and `run_chatbot()`).
- **Control Flow (`if/elif/else`)**: Implementing decision logic for rule-based matching.
- **Loops (`while True`, `break`)**: Sustaining continuous chat until an exit command is provided.

---

## How to Run the Program

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd TASK4_Basic_Chatbot
   ```
3. Run the script using Python:
   ```bash
   python chatbot.py
   ```

---

## Example Conversation

```text
==================================================
       Welcome to the Basic Python Chatbot!
==================================================
Type 'help' to see available commands or 'bye' to quit.

You: hello
Bot: Hi! How can I help you?
You: how are you
Bot: I'm doing great! How are you?
You: what is your name
Bot: I'm a simple Python chatbot.
You: tell me a joke
Bot: Sorry, I don't understand that.
You: help
Bot: Available commands:
  - hello            : Greet the chatbot
  - hi               : Friendly greeting
  - how are you      : Ask about chatbot status
  - what is your name: Ask chatbot's name
  - help             : Show this help menu
  - bye              : Exit the chatbot
You: bye
Bot: Goodbye! Have a great day!
```
