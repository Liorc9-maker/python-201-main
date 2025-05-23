def greet(greeting : str, name : str) -> str:
    """Generates a greeting.

    Args:
        greeting (str): The greeting to use, e.g., "Hello"
        name (str): The name of the person you want to greet`

    Returns:
        str: A personalized greeting message
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence
print(greet("Hi", "Jo"))