import os
import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("File name: ")
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':
    main()
