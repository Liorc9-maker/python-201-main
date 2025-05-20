# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
from pathlib import Path

words_reverse = []


file_in = Path(__file__).parent / 'words.txt'
file_out = Path(__file__).parent / 'words_reverse.txt'

with file_in.open("r") as f:
    lines = f.readlines()
    for line in reversed(lines):
        reversed_line = ' '.join(line.strip().split())
        words_reverse.append(reversed_line)

with file_out.open("w") as w:
    for line in words_reverse:
        w.write(line + '\n')