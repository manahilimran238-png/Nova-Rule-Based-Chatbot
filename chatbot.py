import random
from responses import RESPONSES


def get_response(intent):
    """Select a response from the knowledge base."""
    return random.choice(RESPONSES[intent])


def normalize_input(user_input):
    """Normalize common informal words and spacing."""

    replacements = {
        "u": "you",
        "ur": "your",
        "wat": "what",
        "wht": "what",
        "pls": "please",
        "plz": "please",
        "thx": "thanks"
    }

    words = user_input.split()

    normalized_words = [
        replacements.get(word, word)
        for word in words
    ]

    return " ".join(normalized_words)


def detect_intent(user_input):
    """Identify the user's intent using predefined rules."""

    # Additional sanitization
    user_input = normalize_input(user_input)

    # Intent 1: Greeting
    greeting_words = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if any(word in user_input for word in greeting_words):
        return "greeting"

    # Intent 2: How are you
    if "how are you" in user_input:
        return "how_are_you"

    # Intent 3: Name
    name_patterns = [
        "your name",
        "who are you",
        "what are you called",
        "can i get your name",
        "tell me your name"
    ]

    if any(pattern in user_input for pattern in name_patterns):
        return "name"

    # Intent 4: Capabilities
    capability_patterns = [
        "what can you do",
        "what do you do",
        "your capabilities",
        "your features",
        "what are you able to do"
    ]

    if any(pattern in user_input for pattern in capability_patterns):
        return "capabilities"

    # Intent 5: Thanks
    thanks_patterns = [
        "thanks",
        "thank you",
        "thankyou"
    ]

    if any(pattern in user_input for pattern in thanks_patterns):
        return "thanks"

    # Intent 6: Help
    help_patterns = [
        "help",
        "can you help me",
        "could you help me",
        "i need help"
    ]

    if any(pattern in user_input for pattern in help_patterns):
        return "help"

    # Intent 7: Goodbye
    exit_commands = [
        "bye",
        "goodbye",
        "exit",
        "quit",
        "see you"
    ]

    if any(command in user_input for command in exit_commands):
        return "goodbye"

    # Fallback
    return "unknown"


def chatbot():
    """Run the continuous chatbot conversation."""

    print("=" * 55)
    print("🤖 NOVA - RULE-BASED AI ASSISTANT")
    print("=" * 55)
    print("Type 'help' for available commands.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("-" * 55)

    # INPUT LOOP: continuous while cycle
    while True:

        # SANITIZATION: handle case and whitespace
        user_input = input("You: ").lower().strip()

        # Detect user intent
        intent = detect_intent(user_input)

        # Generate response from knowledge base
        response = get_response(intent)

        print("Nova:", response)

        # EXIT STRATEGY: clean break command
        if intent == "goodbye":
            break


if __name__ == "__main__":
    chatbot()