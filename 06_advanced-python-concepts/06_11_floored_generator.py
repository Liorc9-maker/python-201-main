# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?
nums = range(1, 1000000)
gen = (i for i in nums if i % 1111 == 0)
for dig in gen:
    print(dig // 1111)