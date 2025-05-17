# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

result={}
num = 1
while num <=10:
    result[num] = num * num
    num += 1

print(result)    

same_result = {num_else: num_else * num_else for num_else in range(1,11)}
print(same_result)