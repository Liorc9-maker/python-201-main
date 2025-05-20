# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
from pathlib import Path


file_in = Path(__file__).parent / 'words.txt'

with file_in.open("r") as f:
    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word) 