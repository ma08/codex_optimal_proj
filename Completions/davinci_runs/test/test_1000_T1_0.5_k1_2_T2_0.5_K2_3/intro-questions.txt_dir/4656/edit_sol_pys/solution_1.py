import os
import sys


def main():
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        print("File path {} does not exist. Exiting...".format(file_name))
        sys.exit()

    lines = []
    with open(file_name) as f:
        lines = f.readlines()

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
