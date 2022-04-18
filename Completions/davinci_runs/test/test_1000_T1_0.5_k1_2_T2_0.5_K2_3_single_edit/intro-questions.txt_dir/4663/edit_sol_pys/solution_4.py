

import sys

def get_numbers(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers


def main():
    filename = sys.argv[1]
    numbers = get_numbers(filename)
    print(numbers)


if __name__ == "__main__":
    main()
