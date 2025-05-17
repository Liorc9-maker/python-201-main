# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Step 1: Sort the list
randlist.sort()

# Step 2: Prepare a list for storing tuples
tuple_list = []

# Step 3: If there's an odd number of elements, add a 0 at the end
if len(randlist) % 2 != 0:
    randlist.append(0)

# Step 4: Loop through the list two items at a time
for num in range(0, len(randlist), 2):
    pair = (randlist[num], randlist[num + 1])
    tuple_list.append(pair)

# Step 5: Print each tuple
for t in tuple_list:
    print(t)
       