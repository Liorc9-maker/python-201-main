# Convert a string to a tuple and print out the result.
string = tuple("codingnomads")
print(string)
# What do you see?
# the outpus is: ('c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's')
# What happens if you try to iterate over your tuple of characters?
for char in string:
    print(char)

#  codingnomads's each letter is outputed in a seperate line.
 
# Do you notice any difference to iterating over the string?

# Both the string and the tuple are iterable, and iterating over either one 
# yields the same individual characters in the same order.
# So functionally, iterating over a string or a tuple of its characters looks the same.
# The main difference lies in the data type:
# A string is a sequence of characters.
# A tuple is an immutable collection, and here it holds individual string elements 
# (each character is still a string of length 1).









