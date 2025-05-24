# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.


def greet(greeting: str, name: str) -> str:
    """Generates a greeting."""
    return f"{greeting} {name},\n\nHow are you?\n"

def write_letter(writer_name: str, recipient_name: str, greeting: str, text: str, goodbye: str) -> str:
    greeting_message = greet(greeting, recipient_name)
    goodbye_message = f"\n\n{goodbye},\n{writer_name}"
    return greeting_message + text + goodbye_message

# Get user inputs
greeting_input = input("💬 Please type in your greeting: ")
recipient_name = input("📨 Please type in the recipient's name: ")
writer_name = input("✒️  Type in your name: ")
letter_body = input("📝 Type in the letter body: ")
goodbye_input = input("✒️  Type in your goodbye text: ")

# Print the full letter
print(write_letter(writer_name, recipient_name, greeting_input, letter_body, goodbye_input))

