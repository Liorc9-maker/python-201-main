'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

#unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
#sorted_list = []

#for x in range(0, len(unsorted_list)):

#    min = unsorted_list[0][1]
#    print(min)
#    index = 0

#    for i in range(0, len(unsorted_list)):
#        if unsorted_list[i][1] < min:
#            min = unsorted_list[i][1]
#            index = i
#    sorted_list.append(unsorted_list[index])
#    unsorted_list.remove(unsorted_list[index])


#print(unsorted_list)
#print(sorted_list)


# Your script is a good manual implementation of selection sort applied to a list of tuples. It works by:
# Finding the tuple with the smallest numeric value.
# Appending it to sorted_list.
# Removing it from unsorted_list.
# Repeating until all elements are sorted.

# However, there are a couple of things to improve:

# Re-initializing min with unsorted_list[0][1] every time is correct, 
# but you’re also initializing index = 0 before the loop and not updating it when unsorted_list[i][1] == min. 
# This can cause issues if there are duplicates.

# The loop for x in range(0, len(unsorted_list)): will not work as expected, because
# len(unsorted_list) changes as you remove() elements. This can result in skipped items or index errors.

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

while unsorted_list:
    # Initialize min value and index
    min_value = unsorted_list[0][1]
    min_index = 0

    for i in range(1, len(unsorted_list)):
        if unsorted_list[i][1] < min_value:
            min_value = unsorted_list[i][1]
            min_index = i

    # Move the smallest tuple to sorted_list
    sorted_list.append(unsorted_list.pop(min_index))

print("Unsorted list:", unsorted_list)
print("Sorted list:", sorted_list)
