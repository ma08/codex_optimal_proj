import sys
from math import sqrt



def main():
    # Read in x and y
    x, y = [int(x) for x in sys.stdin.readline().split()]

    # Calculate the distance between (x, y) and (0, 0)
    dist = sqrt(x * x + y * y)

    # Print the distance
    print(dist)

if __name__ == "__main__":
    main()
