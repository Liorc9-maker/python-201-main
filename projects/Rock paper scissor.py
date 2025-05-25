# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner
import random

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    else:
        return "paper" 
        
def determine_winner(hand1, hand2):
    if hand1 == "scissor":
        if hand2 == "rock":
            print(f"You lose! {hand2} beats {hand1}")
        elif hand2 == "scissor":
            print("It's a tie!")
        else:
            print(f"You win! {hand1} beats {hand2}")
    elif hand1 == "rock":
        if hand2 == "rock":
            print("It's a tie!")
        elif hand2 == "paper":
            print(f"You lose! {hand2} beats {hand1}")
        else:
            print(f"You win! {hand1} beats {hand2}")
    elif hand1 == "paper":
        if hand2 == "paper":
            print("It's a tie!")
        elif hand2 == "rock":
            print(f"You win! {hand1} beats {hand2}")
        else:
            print(f"You lose! {hand2} beats {hand1}")

# Take user input and validate
user_input = int(input("Please type 0 for scissor, 1 for rock, 2 for paper: "))
while user_input > 2 or user_input < 0:
    user_input = int(input("Invalid input. Please type 0 for scissor, 1 for rock, 2 for paper: "))

# Generate computer choice
computer_choice = random.randint(0, 2)

# Convert to hand strings
user_hand = get_hand(user_input)
computer_hand = get_hand(computer_choice)

# Show selections
print(f"\nYou chose: {user_hand}")
print(f"Computer chose: {computer_hand}")

# Determine winner
determine_winner(user_hand, computer_hand)
