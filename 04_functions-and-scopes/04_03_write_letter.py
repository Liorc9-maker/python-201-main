# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, text):
    greeting = f"Dear {name},\n\n"
    goodbye = f"\n\nSincerely,\n{name}"
    letter = greeting + text + goodbye
    return letter

name_input = input("✒️  Type in a name: ")
letter_body = input("📝 Type in the letter body: ")

print(write_letter(name_input, letter_body))
