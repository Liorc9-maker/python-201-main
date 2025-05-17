#Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
#Create an inventory for your player, where they can add and remove items.
#Players should be able to collect items they find in rooms and add them to their inventory.
#If they lose a fight against the dragon, then they should lose their inventory items.
#Add more rooms to your game and allow your player to explore.
#Some rooms can be empty, others can contain items, and yet others can contain an opponent.
#Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
#Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an 
# effect on whether your player wins or loses when battling an opponent.

door_options = {"left", "right"}
look_options = {"return", "look around"}
sword_options = {"yes", "no"}
dragon_options = {"fight", "return"}
inventory = []


player = input("Please type your name: ")
print(f"Hello {player}. \nWelcome to the game world!")

door = (input("Choose between the left or the right door. \nType right/left: ").lower())
while door not in door_options:
    door = input("Invalid choice. Type right or left: ").lower()

has_sword = False
while True:
    if door == "left":
        left_choice = (input("You see an empty room. \nType return/look around: ").lower())
        while left_choice not in look_options:
            left_choice = input("Invalid choice. Type return/look around: ").lower()    

        if left_choice == "look around":
            print("You look around the empty room and find a sword.")
            sword_choice = input("Take the sword or leave it? \nType yes/no: ").lower()
            while sword_choice not in sword_options:
                sword_choice = input("Invalid choice. Type yes/no: ").lower()

            if sword_choice == "yes":
                has_sword = True
                print("You returned and entered the right door. You see a dragon in the room.")
                door = "right"
            else:
                continue  # Loop back to left room

        elif left_choice == "return":
            door = "right"

    elif door == "right":
        print("You see a dragon in the room.")
        dragon_choice = input("Fight the dragon or return? \nType fight/return: ").lower()
        while dragon_choice not in dragon_options:
            dragon_choice = input("Invalid choice. Type fight/return: ").lower()

        if dragon_choice == "fight":
            if has_sword:
                print("You fight the dragon with your sword. You won!!!")
            else:
                print("You tried to fight the dragon bare-handed. You've been eaten! \nYou lost.")
            break
        elif dragon_choice == "return":
            door = "left"