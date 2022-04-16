import os
import sys


def main():
    print(sys.argv)
    if len(sys.argv) == 1:
        print("File name missing")
    else:
        if os.path.isfile(sys.argv[1]):
            print("File exists")
        else:
            print("File not found")


if __name__ == "__main__":
    main()
