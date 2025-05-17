# Write a script that takes a sentence from the user and returns:
# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

# Note: ignore all spaces.
# Example input:

# I love to work with dictionaries!

# Example output:
# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28
import string


user_input = input("Enter a sentence to analyze:")
cleared_input = user_input.replace(" ", "")

count_dictionary = {
    "Upper case:" : 0,
    "Lower case:" : 0,
    "Punctuation:" : 0,
    "Total chars:" : 0
}

for char in cleared_input:
    if char.isupper():
        count_dictionary["Upper case:"] += 1
    elif char.islower():
        count_dictionary["Lower case:"] += 1
    elif char in string.punctuation:
        count_dictionary["Punctuation:"] += 1

count_dictionary["Total chars:"] = len(cleared_input)
print(user_input)
for key, value in count_dictionary.items():
    print(f"{key}: {value}")
