

import sys

def main():
    numbers = list(map(int, sys.stdin.readline().split(" ")))
    numbers.sort()
    difference = numbers[1] - numbers[0]
    if numbers[2] - numbers[1] == difference:
        print(numbers[2] + difference)
    elif numbers[1] - numbers[0] == difference:
        print(numbers[0] - difference)
    else:
        print(numbers[1] + difference)


if __name__ == "__main__":
    main()
