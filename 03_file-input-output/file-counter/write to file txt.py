# Above this would be your file counter code
# This code snippet assumes you're saving the count
# to a dictionary called `count`, e.g.:
count = {'': 8, '.csv': 2, '.md': 2, '.png': 11}

# New code that writes to a file
file_out = open("filecounts.txt", "w")
file_out.write(str(count))
file_out.close()
