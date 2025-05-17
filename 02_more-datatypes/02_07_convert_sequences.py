# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
string = "codingnomads"
into_tuple = tuple(string)
print(string, into_tuple, type(into_tuple))
# - Convert the tuple into a list.
into_list = list(into_tuple)
print(into_list, type(into_list))
# - Change the `c` character in your list into a `k`
into_list[0] = "k"
print(into_list)
# - Convert the list back into a tuple.
into_tuple = tuple(into_list)
print(into_tuple, type(into_tuple))
