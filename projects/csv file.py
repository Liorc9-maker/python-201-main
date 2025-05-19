import csv
from pathlib import Path

count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

file_path = Path("C:/Users/liorc/Desktop/filecounts.csv")

# Check if file exists and is empty (or doesn't exist yet)
write_headers = not file_path.exists() or file_path.stat().st_size == 0

with file_path.open("a", newline='') as csvfile:
    countwriter = csv.writer(csvfile)

    if write_headers:
        headers = ["(no extension)", ".csv", ".md", ".png"]
        countwriter.writerow(headers)

    # Write the values in the order of the headers
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)
