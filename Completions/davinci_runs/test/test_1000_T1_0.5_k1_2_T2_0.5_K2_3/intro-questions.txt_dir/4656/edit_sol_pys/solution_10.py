import os
import sys


def main():
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        print("File path {} does not exist. Exiting...".format(file_name))
        sys.exit()

    with open(file_name) as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    main()
