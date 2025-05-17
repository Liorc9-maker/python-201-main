# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [] # Will hold the final flat list.
stack = [starter_list] # is a list we'll use to simulate recursion. It starts with the original nested list inside it.

while stack:  #Keep going as long as there’s something in the stack.
    current = stack.pop()  #Remove the last item from the stack.
    if isinstance(current, list):  # If it's a []
        stack.extend(reversed(current))  # Add items in correct order
    else:
        flattened_list.append(current) # If it's a number just add it.

print(flattened_list)

