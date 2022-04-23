
import sys
import os


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Sorry, this file does not exist")


def write_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
    except FileNotFoundError:
        print("Sorry, this file does not exist")


def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("Sorry, this file does not exist")


def main():
    filename = sys.argv[1]
    if len(sys.argv) == 2:
        read_file(filename)
    elif len(sys.argv) == 3:
        write_file(filename, sys.argv[2])
    elif len(sys.argv) == 4:
        delete_file(filename)


if __name__ == '__main__':
    main()
