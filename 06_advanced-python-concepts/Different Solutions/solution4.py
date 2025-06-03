'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

# unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
# sorted_list = []


#for tup in list(unsorted_list):

#    current_min = unsorted_list[0][1]
#    index = 0

#    for i in range(0, len(unsorted_list)):
#        if unsorted_list[i][1] < current_min:
#            current_min = unsorted_list[i][1]
#            index = i
#    sorted_list.append(unsorted_list[index])
#    unsorted_list.remove(unsorted_list[index])

#print(unsorted_list)
#print(sorted_list)

# Pros:
# Functional and produces the correct sorted output.
# Logic is easy to follow and good for learning how sorting works manually.

# Minor Note:
# The line for tup in list(unsorted_list): is only used to control the number of iterations, since the
# unsorted_list gets shorter each time. While this works, it's slightly misleading since tup is never used
# inside the loop.
# You can simplify by using a while loop instead:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

while unsorted_list:
    current_min = unsorted_list[0][1]
    index = 0

    for i in range(1, len(unsorted_list)):
        if unsorted_list[i][1] < current_min:
            current_min = unsorted_list[i][1]
            index = i

    sorted_list.append(unsorted_list.pop(index))

print("Unsorted list:", unsorted_list)
print("Sorted list:", sorted_list)
