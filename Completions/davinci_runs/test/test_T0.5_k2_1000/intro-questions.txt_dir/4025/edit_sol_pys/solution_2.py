
import sys

def main():
    # Read in data
    a, b, c = [int(x) for x in sys.stdin.readline().split()] 

    # Calculate the maximum number of days the cat can eat on a trip
    # without additional food purchases
    days = min(a, b, c)

    # Print the result
    print(days * 7)

if __name__ == "__main__":
    main()
