'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

#Sunsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
#sorted_list = []

#value_list = []
#for tuple_ in unsorted_list:
#    value_list.append(tuple_[1])

#print(value_list)
#value_list.sort()

#for value in value_list:
#    for tuple_ in unsorted_list:
#        if tuple_[1] == value:
#            sorted_list.append(tuple_)
#            unsorted_list.remove(tuple_)
#            break

#print(sorted_list)


# Your script correctly sorts the list of tuples based on the numerical value in each tuple. You're doing this by:
#Extracting all the numerical values.
#Sorting those values.
#Iterating over the sorted values and matching them back to the tuples.

# However, there are a few issues and possible improvements:
# Modifying unsorted_list while iterating over it can lead to unexpected behavior or bugs. 
# Fortunately, your use of break prevents major issues here, but it's still risky and not ideal.
# The algorithm becomes inefficient for larger lists due to nested loops and remove() operations.
# It does not handle duplicates well (if two tuples had the same number, one might get lost or skipped).

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

# Create a copy of the unsorted list to avoid modifying it during iteration
temp_unsorted = unsorted_list.copy()

# Extract and sort the values
value_list = [t[1] for t in temp_unsorted]
value_list.sort()

# Match sorted values to tuples
for value in value_list:
    for tuple_ in temp_unsorted:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            temp_unsorted.remove(tuple_)
            break

print("Sorted list:", sorted_list)

