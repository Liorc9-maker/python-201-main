'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

#unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
#sorted_list = []

#while we still have values in the unsorted list
#while len(unsorted_list) > 0:
    #loop through the unsorted list to find the minimum value
 #   current_value = unsorted_list[0][1]
  #  min_value = unsorted_list[0][1]
   # index = 0
   # for tuple_ in unsorted_list:
        #save the minimum value to use outside of this for loop
    #    if tuple_[1] <= min_value:
     #       min_value = tuple_[1]
      #      min_index = index
      #  index += 1

    #push the minimum value onto the sorted list
   # sorted_list.append(unsorted_list.pop(min_index))
    #print("unsorted list is " + str(unsorted_list))

#print(sorted_list)

#Your script is a correct manual implementation of selection sort for sorting a list of tuples by their numeric value. 
# However, it can be slightly cleaned up and improved for readability and efficiency.
#also the printing of the emptying of the unsorted_list is not necessary.

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

# While there are items in the unsorted list
while unsorted_list:
    # Assume the first item is the minimum
    min_index = 0
    for i in range(1, len(unsorted_list)):
        if unsorted_list[i][1] < unsorted_list[min_index][1]:
            min_index = i

    # Move the minimum item to the sorted list
    sorted_list.append(unsorted_list.pop(min_index))
   # print("Unsorted list is:", unsorted_list)

print("Sorted list:", sorted_list)
