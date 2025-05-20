# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
from pathlib import Path


file_in = Path(__file__).parent / 'words.txt'

words_count = 0
max_length = 0
longest_words = []
min_length = None
shortest_words = []




with file_in.open("r") as f:
    for line in f:
        words = line.strip().split()
        words_count += len(line.strip().split())


        for word in words:
            if len(word) > max_length:
                max_length = len(word)
                longest_words = [word]
            elif len(word) == max_length:
                longest_words.append(word)

            if min_length is None or len(word) < min_length:
                min_length = len(word)
                shortest_words = [word]
            elif len(word) == min_length:
                shortest_words.append(word)
                         
print(f"The shortest word(s) are: {shortest_words}")
print(f"The longest word(s) are: {longest_words}")
print(f"The total number of words is: {words_count}")