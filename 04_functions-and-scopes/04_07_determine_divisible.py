# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divisible_or(num):
    result = num % 4 == 0 or num % 7 == 0
    return result


def divisible_and(num):
    result = num % 4 == 0 and num % 7 == 0
    return result

num = int(input("Please type a number between 1 and 1,000,000,000: "))

print(f"🔍 Divisible by 4 or 7: {divisible_or(num)}")
print(f"✅ Divisible by both 4 and 7: {divisible_and(num)}")
      
