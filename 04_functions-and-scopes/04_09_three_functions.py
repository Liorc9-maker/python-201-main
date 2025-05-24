# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

from pathlib import Path

export_path = Path.cwd() / "letter.txt"

def greet(greeting: str, name: str) -> str:
    """Generates a greeting."""
    return f"{greeting} {name},\n\nHow are you?\n"

def write_letter(writer_name: str, recipient_name: str, greeting: str, text: str, goodbye: str) -> str:
    greeting_message = greet(greeting, recipient_name)
    goodbye_message = f"\n\n{goodbye},\n{writer_name}"
    return greeting_message + text + goodbye_message

def save_letter_to_file(writer_name: str, recipient_name: str, greeting: str, text: str, goodbye: str, path: Path) -> None:
    letter = write_letter(writer_name, recipient_name, greeting, text, goodbye)
    path.write_text(letter, encoding="utf-8")
    print(f"Letter saved to {path}")

# Get user inputs
greeting_input = input("💬 Please type in your greeting: ")
recipient_name = input("📨 Please type in the recipient's name: ")
writer_name = input("✒️  Type in your name: ")
letter_body = input("📝 Type in the letter body: ")
goodbye_input = input("✒️  Type in your goodbye text: ")

# Print the full letter
print(write_letter(writer_name, recipient_name, greeting_input, letter_body, goodbye_input))
save_letter_to_file(writer_name, recipient_name, greeting_input, letter_body, goodbye_input, export_path)