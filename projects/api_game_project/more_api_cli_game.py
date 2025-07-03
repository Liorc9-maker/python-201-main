import requests
import random
import json
import os

def setup_game_name_and_quote():
    global game_name, quote, author
    while True:
        internet_on = input("Do you have an internet connection?\nType 1 for yes or 2 for no: ")

        if internet_on == "1":
            try:
                min_len = 4
                max_len = 6
                URL = f"https://uzby.com/api.php?min={min_len}&max={max_len}"
                response = requests.get(URL)
                game_name = response.text

                response_quote = requests.get("https://zenquotes.io/api/random")
                data = response_quote.json()

                quote = data[0]['q']
                author = data[0]['a']
                break
            except requests.RequestException as e:
                print("Error fetching data. Please check your connection.")
                print(e)
        elif internet_on == "2":
            print("Skipping online features. No random name or quote will be used.")
            game_name = "Sreenath"
            quote = "Even a broken watch is correct twice a day."
            author = "Brian Selznick"
            break
        else:
            print("Invalid choice. Please type 1 or 2.")

# --- Constants ---
door_options = {"left", "right", "forward", "armory", "cave"}
look_options = {"return", "look around"}
yes_no_options = {"yes", "no"}
battle_options = {"fight", "return"}
save_file = "game_state.json"

# --- Game State ---
inventory = []
goblin_defeated = False
player = ""

# --- Utility Functions ---
def load_game():
    """Checks for a saved file and loads player name, 
       inventory, and goblin status  
    """
    global inventory, goblin_defeated, player
    if os.path.exists(save_file):
        with open(save_file, "r") as f:
            state = json.load(f)
            inventory = state.get("inventory", [])
            goblin_defeated = state.get("goblin_defeated", False)
            player = state.get("player", "")
            print(f"Game loaded for {player}.")
            print("For the game, a unique, pronounceable name will be assigned to you...")
            print(f"Welcome {game_name}!")
            print("Win the game for a quote of wisdom!")
    else:
        player = input("Please type your name: ")
        print(f"Hello {player}.\nWelcome to the game world!")
        print("For the game, a unique, pronounceable name will be assigned to you..")
        print(f"Welcome {game_name}!")
        print("Win the game for a quote of wisdom!")

def save_game():
    """Writes the player's current inventory, 
       name, and goblin status to file.
    """
    with open(save_file, "w") as f:
        json.dump({
            "player": player,
            "inventory": inventory,
            "goblin_defeated": goblin_defeated
        }, f)
    print("Game state saved.")

def prompt_direction():
    """Asks the player where to go next, 
       checks that the input is valid.

    Returns:
        str : Where the player goes next.
    """
    choice = input("Where to next? left/right/forward/armory/cave: ").strip().lower()
    while choice not in door_options:
        choice = input("Invalid choice. Choose left/right/forward/armory/cave: ").strip().lower()
    return choice

# --- Room Functions ---
def room_left():
    """Asks the player his choices regarding
       the left room. look around/return, the
       player can also find a sword.
       Also it checks whether the sword if 
       already in the inventory.
    """
    print("You enter a dusty old room.")
    choice = input("Type return/look around: ").strip().lower()
    while choice not in look_options:
        choice = input("Invalid choice. Type return/look around: ").strip().lower()

    if choice == "look around" and "sword" not in inventory:
        print("You found a sword!")
        take = input("Do you want to take it? yes/no: ").strip().lower()
        if take == "yes":
            inventory.append("sword")
            print("You took the sword.")
    elif choice == "look around":
        print("There's nothing else here.")

def room_right():
    """Gives the player the choices of 
       the right room + the option to find a potion.
       the function checks if the player has it already in his inventory.
    """
    print("You entered into a library. Dusty books line the shelves.")
    choice = input("Type return/look around: ").strip().lower()
    while choice not in look_options:
        choice = input("Invalid choice. Type return/look around: ").strip().lower()

    if choice == "look around" and "potion" not in inventory:
        print("You find a glowing potion on a dusty shelf.")
        take = input("Do you want to take the potion? yes/no: ").strip().lower()
        if take == "yes":
            inventory.append("potion")
            print("You took the potion.")
    elif choice == "look around":
        print("You've already taken the potion. There's nothing else here.")

def room_armory():
    """Gives the player the opcions of the armory,
       player has a chance of finding a sturdy shield.
       The function also checkes whether the player already has it 
       in his inventory.
    """
    print("You enter the old armory.")
    choice = input("Type return/look around: ").strip().lower()
    while choice not in look_options:
        choice = input("Invalid choice. Type return/look around: ").strip().lower()

    if choice == "look around" and "shield" not in inventory:
        print("You find a sturdy shield on the wall.")
        take = input("Do you want to take the shield? yes/no: ").strip().lower()
        if take == "yes":
            inventory.append("shield")
            print("You took the shield.")
    elif choice == "look around":
        print("There's nothing else here.")

def room_cave():
    """Checks if the goblin was already defeated.
       if no than player can look around, encounter the goblin
       and fight or return. saves the game to file if player is defeated.
    """
    global goblin_defeated
    print("You enter a dark, musty cave.")
    if goblin_defeated:
        print("The goblin you defeated earlier lies still. The cave is quiet now.")
        return

    choice = input("Type return/look around: ").strip().lower()
    while choice not in look_options:
        choice = input("Invalid choice. Type return/look around: ").strip().lower()

    if choice == "look around":
        print("You hear growling... A goblin jumps out!")
        action = input("Fight the goblin or return? fight/return: ").strip().lower()
        while action not in battle_options:
            action = input("Invalid choice. Type fight/return: ").strip().lower()

        if action == "fight":
            result = battle("goblin")
            if result:
                goblin_defeated = True
                print("You defeated the goblin!")
            else:
                print("The goblin defeated you! You lost all your items!")
                inventory.clear()
                print("Game over.")
                save_game()
                exit()

def room_forward():
    """Gives the player the option to fight the dragon or return.
       saves the game state if player is defeated.
    """
    print("You step into a massive chamber. A DRAGON roars!")
    action = input("Fight the dragon or return? fight/return: ").strip().lower()
    while action not in battle_options:
        action = input("Invalid choice. Type fight/return: ").strip().lower()

    if action == "fight":
        result = battle("dragon")
        if result:
            print("You slayed the dragon! You are the true hero!")
            print(f'\nHere is your quote of wisdom:\n"{quote}" \n-{author}')
        else:
            print("The dragon defeated you... Your journey ends here.")
            inventory.clear()
            print("Game over.")
        save_game()
        exit()

# --- Battle Logic ---
def battle(opponent):
    """Manages the battle with the enemies.
        using the random option each player arandom number. the one with the higher
        number wins the battle. It also includes the value of the items in the inventory.

    Args:
        opponent (str): The dragon is stronger than the goblin

    Returns:
        int: returns the result of the battle.

    """
    has_sword = "sword" in inventory
    has_shield = "shield" in inventory
    has_potion = "potion" in inventory

    player_roll = random.randint(1, 6)
    opp_roll = random.randint(1, 4 if opponent == "goblin" else 6)

    player_power = player_roll + (3 if has_sword else 0) + (2 if has_shield else 0) + (1 if has_potion else 0)
    opp_power = opp_roll + (2 if opponent == "goblin" else 5)

    print(f"Your score: {player_power} (Roll: {player_roll})")
    print(f"{opponent.capitalize()}'s score: {opp_power} (Roll: {opp_roll})")

    return player_power >= opp_power

# --- Main Game Loop ---
def main():
    """Loads the game state.
       Asks where the player wants to go.
       Calls the function for that room.
       saves the game after that action.
       Loads the game state.
   """
    setup_game_name_and_quote()
    load_game()
    while True:
        direction = prompt_direction()

        if direction == "left":
            room_left()
        elif direction == "right":
            room_right()
        elif direction == "armory":
            room_armory()
        elif direction == "cave":
            room_cave()
        elif direction == "forward":
            room_forward()

        save_game()

# --- Start Game ---
if __name__ == "__main__":
    main()
