import csv
import os

if __name__ == "__main__":
    with open('test.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
