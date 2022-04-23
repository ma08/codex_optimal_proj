
import os
import sys

def main():
    if len(sys.argv) == 1:
        print("Please pass the file name as an argument")
        sys.exit()

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print("File does not exist")
        sys.exit()

    if not os.access(filename, os.R_OK):
        print("You do not have access to read this file")
        sys.exit()

    with open(filename, 'r') as file:
        for line in file.readlines():
            print(line)
    pass


if __name__ == "__main__":
    main()
