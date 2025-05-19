import pathlib
import pprint
import csv
from pathlib import Path  # This was missing!

# Step 1: Define the path to the Desktop
desktop = Path("C:/Users/liorc/Desktop")  # Use Windows path format for consistency

# Step 2: Count files by extension
counter = {}
for file in desktop.iterdir():
    if file.is_file():
        ext = file.suffix.lower() or "(no extension)"  # Handle files with no extension
        counter[ext] = counter.get(ext, 0) + 1
    elif file.is_dir():
        counter['<DIR>'] = counter.get('<DIR>', 0) + 1

# Step 3: Sort and print
sorted_counter = dict(sorted(counter.items()))
pprint.pprint(sorted_counter)

# Step 4: Prepare to write to CSV
csv_path = Path("C:/Users/liorc/Desktop/filecounts.csv")
write_headers = not csv_path.exists() or csv_path.stat().st_size == 0

with csv_path.open("a", newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write headers (keys) if file is new/empty
    if write_headers:
        writer.writerow(sorted_counter.keys())

    # Write one row of values (counts)
    writer.writerow(sorted_counter.values())
