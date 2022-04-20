import os
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python file.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print("Path does not exist")
        sys.exit(1)

    if os.path.isfile(path):
        print("File")
        print(os.path.getsize(path))
    elif os.path.isdir(path):
        print("Directory")
        print(os.listdir(path))
    else:
        print("Something else")


if __name__ == "__main__":
    main()
