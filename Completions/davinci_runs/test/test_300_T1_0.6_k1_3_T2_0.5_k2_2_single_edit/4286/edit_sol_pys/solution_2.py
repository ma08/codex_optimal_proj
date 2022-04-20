
from sys import argv
import csv


def main():
    with open(argv[1]) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
