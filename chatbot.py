"""
TASK 4: Basic Chatbot
Description: A simple rule-based console chatbot built with pure Python.
Author: Python Learning Project
"""


def get_response(user_input):
    """
    Returns the chatbot's response for a given user message.
    Uses if/elif/else conditions to match predefined rules.
    """
    if user_input == "hello":
        return "Hi! How can I help you?"
    elif user_input == "hi":
        return "Hello! Nice to meet you."
    elif user_input == "how are you":
        return "I'm doing great! How are you?"
    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."
    elif user_input == "help":
        return (
            "Available commands:\n"
            "  - hello            : Greet the chatbot\n"
            "  - hi               : Friendly greeting\n"
            "  - how are you      : Ask about chatbot status\n"
            "  - what is your name: Ask chatbot's name\n"
            "  - help             : Show this help menu\n"
            "  - bye              : Exit the chatbot"
        )
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    else:
        # Fallback response for any unknown or unsupported input
        return "Sorry, I don't understand that."


def run_chatbot():
    """
    Runs the main conversation loop.
    Continuously prompts the user for input until 'bye' is entered.
    """
    # Welcome banner
    print("=" * 50)
    print("       Welcome to the Basic Python Chatbot!")
    print("=" * 50)
    print("Type 'help' to see available commands or 'bye' to quit.\n")

    # While loop for continuous interaction
    while True:
        # Take input from user
        user_input = input("You: ")

        # Clean user input: remove leading/trailing spaces and make lowercase
        cleaned_input = user_input.strip().lower()

        # Get response using rule-based function
        bot_response = get_response(cleaned_input)

        # Display chatbot response
        print(f"Bot: {bot_response}")

        # If user typed 'bye', exit the conversation loop
        if cleaned_input == "bye":
            break


# Entry point of the script
if __name__ == "__main__":
    run_chatbot()
