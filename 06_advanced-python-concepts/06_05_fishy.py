# Using a listcomp, create a list from the following tuple that includes
# only words ending with -fish. Tip: Use an `if` statement in the listcomp.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
listcomp = [word for word in fish_tuple if word.endswith('fish')]
#print(listcomp)