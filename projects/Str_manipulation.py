from pathlib import Path
import ast

# Define the path using pathlib
file_path = Path(r"C:\Users\liorc\Desktop\filecounts.txt")

# Read the file
contents = file_path.read_text().strip()

# Parse the string as a dictionary
data = ast.literal_eval(contents)

key = '.jpg'
print(f"Key: {key}, Value: {data[key]}")