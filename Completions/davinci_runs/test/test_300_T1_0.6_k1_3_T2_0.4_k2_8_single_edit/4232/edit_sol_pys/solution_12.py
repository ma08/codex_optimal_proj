import os
import sys
import re


def main():
    if len(sys.argv) != 2:
        print("Usage: python file.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print("Path does not exist")
        sys.exit(1)

    if not os.path.isfile(path):
        print("Path is not a file")
        sys.exit(1)

    with open(path, "r") as f:
        for line in f:
            if re.match(r'^#.*', line):
                print("Comment")
            elif re.match(r'^[a-zA-Z_]+[a-zA-Z0-9_]*\s*=.*', line):
                print("Assignment")
            elif re.match(r'^[a-zA-Z_]+[a-zA-Z0-9_]*\s*\(.*', line):
                print("Function definition")
            else:
                print("Other")


if __name__ == "__main__":
    main()
