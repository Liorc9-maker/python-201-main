# Use the `csv` module to read in and count the different file types.
# analyze.py
import csv
from pathlib import Path

file_path = Path(__file__).parent /"filecounts.csv"

with file_path.open("r", newline = '') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)
