#Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
#Create an inventory for your player, where they can add and remove items.
#Players should be able to collect items they find in rooms and add them to their inventory.
#If they lose a fight against the dragon, then they should lose their inventory items.
#Add more rooms to your game and allow your player to explore.
#Some rooms can be empty, others can contain items, and yet others can contain an opponent.
#Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
#Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an 
# effect on whether your player wins or loses when battling an opponent.

import random

# Valid user input options
door_options = {"left", "right", "forward", "armory", "cave"}
look_options = {"return", "look around"}
yes_no_options = {"yes", "no"}
battle_options = {"fight", "return"}

# Inventory
inventory = []

goblin_defeated = False


# Player setup
player = input("Please type your name: ")
print(f"Hello {player}.\nWelcome to the game world!")

# Start the adventure
door = input("Choose a direction: left/right/forward/armory/cave: ").strip().lower()
while door not in door_options:
    door = input("Invalid choice. Choose left/right/forward/armory/cave: ").strip().lower()

# Game loop
while True:
    if door == "left":
        print("You enter a dusty old room.")
        left_choice = input("Type return/look around: ").strip().lower()
        while left_choice not in look_options:
            left_choice = input("Invalid choice. Type return/look around: ").strip().lower()

        if left_choice == "look around":
            if "sword" not in inventory:
                print("You found a sword!")
                sword_choice = input("Do you want to take it? yes/no: ").strip().lower()
                while sword_choice not in yes_no_options:
                    sword_choice = input("Invalid choice. Type yes/no: ").strip().lower()
                if sword_choice == "yes":
                    inventory.append("sword")
                    print("You took the sword.")
            else:
                print("There's nothing else here.")
        door = input("Where to next? left/right/forward/armory/cave: ").strip().lower()

    elif door == "right":
        print("You entered into a library. Dusty books line the shelves.")
        right_choice = input("Type return/look around: ").strip().lower()
        while right_choice not in look_options:
            right_choice = input("Invalid choice. Type return/look around: ").strip().lower()

        if right_choice == "look around":
            print("You find a glowing potion on a dusty shelf.")
            if "potion" not in inventory:
                potion_choice = input("Do you want to take the potion? yes/no: ").strip().lower()
                while potion_choice not in yes_no_options:
                    potion_choice = input("Invalid choice. Type yes/no: ").strip().lower()
                if potion_choice == "yes":
                    inventory.append("potion")
                    print("You took the potion.")
            else:
                print("You’ve already taken the potion. There’s nothing else here.")
        door = input("Where to next? left/right/forward/armory/cave: ").strip().lower()


    elif door == "armory":
        print("You enter the old armory.")
        armory_choice = input("Type return/look around: ").strip().lower()
        while armory_choice not in look_options:
            armory_choice = input("Invalid choice. Type return/look around: ").strip().lower()

        if armory_choice == "look around":
            if "shield" not in inventory:
                print("You find a sturdy shield on the wall.")
                shield_choice = input("Do you want to take the shield? yes/no: ").strip().lower()
                while shield_choice not in yes_no_options:
                    shield_choice = input("Invalid choice. Type yes/no: ").strip().lower()
                if shield_choice == "yes":
                    inventory.append("shield")
                    print("You took the shield.")
            else:
                print("There’s nothing else here.")
        door = input("Where to next? left/right/forward/armory/cave: ").strip().lower()


    elif door == "cave":
        print("You enter a dark, musty cave.")
        if goblin_defeated:
            print("The goblin you defeated earlier lies still. The cave is quiet now.")
            door = input("Where to next? left/right/forward/armory/cave: ").strip().lower()
        else:
            cave_choice = input("Type return/look around: ").strip().lower()
            while cave_choice not in look_options:
                cave_choice = input("Invalid choice. Type return/look around: ").strip().lower()

            if cave_choice == "look around":
                print("You hear growling... A goblin jumps out!")
                goblin_choice = input("Fight the goblin or return? fight/return: ").strip().lower()
                while goblin_choice not in battle_options:
                    goblin_choice = input("Invalid choice. Type fight/return: ").strip().lower()

                if goblin_choice == "fight":
                    print("Battle begins!")
                    has_sword = "sword" in inventory
                    has_shield = "shield" in inventory
                    has_potion = "potion" in inventory

                    player_roll = random.randint(1, 6)
                    goblin_roll = random.randint(1, 4)
                    player_power = player_roll + (3 if has_sword else 0) + (2 if has_shield else 0) + (1 if has_potion else 0)
                    goblin_power = goblin_roll + 2

                    print(f"Your score: {player_power} (Roll: {player_roll})")
                    print(f"Goblin's score: {goblin_power} (Roll: {goblin_roll})")

                    if player_power >= goblin_power:
                        print("You defeated the goblin!")
                        goblin_defeated = True
                        door = input("Where to next? left/right/forward/armory/cave: ").strip().lower()
                    else:
                        print("The goblin defeated you! You lost all your items!")
                        inventory.clear()
                        print("Game over.")
                        break
                else:
                    door = input("Where to next? left/right/forward/armory/cave: ").strip().lower()


    elif door == "forward":
        print("You step into a massive chamber. A DRAGON roars!")
        dragon_choice = input("Fight the dragon or return? fight/return: ").strip().lower()
        while dragon_choice not in battle_options:
            dragon_choice = input("Invalid choice. Type fight/return: ").strip().lower()

        if dragon_choice == "fight":
            print("The final battle begins!")
            has_sword = "sword" in inventory
            has_shield = "shield" in inventory
            has_potion = "potion" in inventory

            player_roll = random.randint(1, 6)
            dragon_roll = random.randint(1, 6)
            player_power = player_roll + (3 if has_sword else 0) + (2 if has_shield else 0) + (1 if has_potion else 0)
            dragon_power = dragon_roll + 6  # Stronger base power

            print(f"Your score: {player_power} (Roll: {player_roll})")
            print(f"Dragon's score: {dragon_power} (Roll: {dragon_roll})")

            if player_power >= dragon_power:
                print("You slayed the dragon! You are the true hero!")
            else:
                print("The dragon defeated you... Your journey ends here.")
                inventory.clear()
                print("Game over.")
            break
        else:
            door = input("Where to next? left/right/forward/armory/cave: ").strip().lower()
