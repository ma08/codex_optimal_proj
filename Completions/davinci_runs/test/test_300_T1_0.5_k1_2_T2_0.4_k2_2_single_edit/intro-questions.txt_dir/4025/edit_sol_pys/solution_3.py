
import math
import sys

def main():
    # Read in data
    a, b, c = [int(x) for x in input().split()]

    # Calculate the maximum number of days the cat can eat in a trip
    # without additional food purchases
    days = math.floor(min(a, b, c) / 2)

    # Print the result
    print(days * 7)

if __name__ == "__main__":
    main()
