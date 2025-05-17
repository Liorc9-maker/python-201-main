# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.
set_list =set()
points = 5
while len(set_list) <= 11 and points > 0:
    try:
        user_input = int(input("Please enter a number: "))
    except ValueError:
        print("That's not a valid number. try again.")
        continue

    if user_input not in set_list:
        set_list.add(user_input)
        print(f"Added {user_input} to the set.")
        if len(set_list) > 10:         
            print(f"You won!\nYou managed to create a set of more than 10 numbers \n{set_list}")
            break
    else:
        points -=1
        print(f"That number was already used. You lose one point.\nPoints left :{points}")
        if points == 0:
            print("Game over. You ran out of points.")
        
        
                     