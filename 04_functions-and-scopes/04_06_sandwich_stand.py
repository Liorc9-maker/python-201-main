# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread, *args): 
    """Takes a sandwich order.

    Args:
        bread (str): Bread type
        *args (tuple): Description of desired toppings. 

    Returns:
        str: Sandwich description.
    """
    if not args:
        middle = "(nothing inside)"
    else:
        middle = " + ".join(args)
    return f"{bread} + {middle} + {bread}"
    
bread_input = input("🍞 Please type the type of bread: ")
toppings_input = input("🥬 Please type the toppings you would like (comma-separated): ")
toppings_list = [t.strip() for t in toppings_input.split(",") if t.strip()]

print(make_sandwich(bread_input, *toppings_list))