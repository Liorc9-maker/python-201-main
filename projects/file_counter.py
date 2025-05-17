# Add the code for the file counter script that you wrote in the course.
import pathlib
import pprint
# To get that information, write a script that locates your Desktop, 
# fetches all the files that are on there, 
# and counts how many files of each different file type are on your desktop. 
# Use a dictionary to collect this data, 
# and print it to your console at the end in order to get an overview of what is there.




# Find the path to my Desktop
desktop = pathlib.Path('/Users/liorc/Desktop')
counter = {}

# Loop through items on the Desktop
for file in desktop.iterdir():
    if file.is_file():  # Only count files, not folders
        ext = file.suffix.lower()
        counter[ext] = counter.get(ext, 0) + 1
# Move the screenshot there
pprint.pprint(counter)