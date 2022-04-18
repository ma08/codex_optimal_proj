
import sys


def read_file(filename):
    try:
        with open(filename) as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        sys.exit(1)


def main():
    lines = read_file('file.py')
    for line in lines:
        print(line.strip())


if __name__ == '__main__':
    main()
