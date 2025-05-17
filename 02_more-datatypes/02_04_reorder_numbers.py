# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1
user_input_num = []
tries = 0
while tries < 10:
    num_input = int(input("please type in a number: "))
    tries += 1
    user_input_num.append(num_input)
print(user_input_num) 

# Extract 2nd, 4th, 6th, 8th, 10th (index 1,3,5,7,9)
even_positions = [user_input_num[i] for i in range(1, 10, 2)]

# Extract 9th, 7th, 5th, 3rd, 1st (index 8,6,4,2,0)
odd_positions_reversed = [user_input_num[i] for i in range(8, -1, -2)]

# Combine and print
result = even_positions + odd_positions_reversed
output = ",".join(str(x) for x in result)
print(output)