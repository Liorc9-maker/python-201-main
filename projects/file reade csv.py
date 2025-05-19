# analyze.py
import csv
from pathlib import Path

file_path = Path("C:/Users/liorc/Desktop/filecounts.csv")

with file_path.open("r", newline = '') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)
