import os
import sys


def main():
    file_name = sys.argv[1]  # first argument is the file name
    if not os.path.isfile(file_name):  # check if file exists
        print("File path {} does not exist. Exiting...".format(file_name))  # print message
        sys.exit()  # exit the program

    lines = []  # empty list
    with open(file_name) as f:  # open file
        lines = f.readlines()  # read lines

    print(lines)  # print lines


if __name__ == "__main__":
    main()
