# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

user_input = input("Please type something:\n")
result = []
words = user_input.split()
print(words)

for word in words:
    result.append(tuple(word))

print(result)    