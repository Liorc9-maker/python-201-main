# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually


# Convert the list into a set.
list_ = [1, 2, 3, 4, 3, 4, 5]
no_dups_list1 = set(list_)
print(f"Convert the list {list_}\ninto a set {no_dups_list1}")

# Only if the number is not in the no_dubs list it is added.
no_dups = []
for num in list_:
    if num not in no_dups:
        no_dups.append(num)
print(f"Second way with the loop:\nBefore: {list_} \nAfter: {no_dups}")        