# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(num_list):
  # define the function here
    max_num = max(num_list)
    min_num = min(num_list)
    sum_num = sum(num_list)
    average_num = sum_num / len(num_list)
    result = f"""The maximum number is: {max_num} 
The minimum number is: {min_num}
The sum of all numbers is: {sum_num}
The average of all numbers is: {average_num}"""
    return result

# call the function below here
print(stats(example_list))
