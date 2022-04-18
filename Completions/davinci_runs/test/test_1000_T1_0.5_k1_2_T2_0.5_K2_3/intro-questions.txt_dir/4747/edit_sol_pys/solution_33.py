

import sys

def main():
    # Read the input and split it into separate integers
    numbers = sys.stdin.readline().split()

    # Compute the sum of the integers
    sum = 0
    for number in numbers:
        sum += int(number)

    # Print the sum
    print(sum)

if __name__ == '__main__':
    main()
