def greet(greeting, name):
    """Generates a greeting.

    Args:
        greeting (str): The greeting to use, e.g., "Hello"
        name (str): The name of the person you want to greet

    Returns:
        str: A personalized greeting message
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence
greeting_input = input("Please type in your greeting: ")
name_input = input("Please type in a name: ")
print(greet(greeting_input, name_input))