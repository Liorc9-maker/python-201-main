# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.
gen = (x for x in range(5))
print(gen, type(gen))
for num in gen:
    print(num)
