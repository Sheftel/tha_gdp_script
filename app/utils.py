import csv
from typing import List


def read_csv(files: List[str]):
    data = []
    for file in files:
        with open(file, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for row in reader:
                data.append(row)
    return data
