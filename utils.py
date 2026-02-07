import argparse
import csv


def read_csv(files):
    data = []
    for file in files:
        with open(file, newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",", quotechar="|")
            for row in reader:
                data.append(row)
    return data


def csvfile(value):
    if not value.endswith(".csv"):
        raise argparse.ArgumentTypeError("argument files must be of type *.csv")
    return value
