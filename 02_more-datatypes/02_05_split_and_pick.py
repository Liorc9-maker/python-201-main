# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.
user_input = input("Please type in something:\n")
text_list = user_input.split()
max_count = 0
most_common = None
for text in text_list:
    count = text_list.count(text)
    if count > max_count:
        max_count = count
        most_common = text
print(most_common)    