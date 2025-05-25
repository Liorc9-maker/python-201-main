# function to capitalize each word
def titlecase(text: str) -> str:
    titlcase = []
    for word in text.split():
        cap_word = word.capitalize()
        titlcase.append(cap_word)
    return " ".join(titlcase)

# collect initial user input
user_input = input("Enter your sentence (type 'exit' to quit): ")
# give output to user
while user_input.lower() != "exit":
    crash_blossom = titlecase(user_input)
    print(crash_blossom)
    # collect user input
    user_input = input("Enter your sentence (type 'exit' to quit): ")