import pathlib


desktop = pathlib.Path('/mnt/c/Users/liorc/Desktop')

file_in = open("filecounts.txt", "r")
contents = file_in.read()


for file in file_in:
    if file.suffix().lower() == ".png":
        print(file)
file_in.close()