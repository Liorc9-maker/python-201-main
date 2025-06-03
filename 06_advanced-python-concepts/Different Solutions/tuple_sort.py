unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
#sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]


#1
#sorted_list = sorted(unsorted_list, key=lambda x: x[1])
#print(list(sorted_list))
#  Great use of `sorted()` with a lambda. This keeps the original list unchanged, which is ideal for many scenarios.


#2
#unsorted_list.sort(key=lambda x: x[1])
#print(unsorted_list)
#  This sorts in place, which is fine if the original order isn't needed later. Consider using `sorted()` if you want to preserve the original list.

#3
#from operator import itemgetter
#sorted_list = sorted(unsorted_list, key=itemgetter(1))
#print(list(sorted_list))
#  Clean use of `itemgetter`. Great for readability, especially when the sort key is an index and used multiple times.


#4
#from functools import partial

#def get_item(index, tup):
#    return tup[index]

# sorted_list = sorted(unsorted_list, key=partial(get_item, 1))
# print(list(sorted_list))
#  Nice use of `functools.partial` to make the key function modular and reusable. This is more flexible for cases where you sort by different tuple indices.
