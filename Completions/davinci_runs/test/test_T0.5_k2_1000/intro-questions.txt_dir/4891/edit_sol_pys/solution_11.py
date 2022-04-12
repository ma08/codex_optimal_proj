

import sys

def main():
    # Get input
    pieces = [int(x) for x in sys.stdin.readline().split()]

    # Check if each piece is in the correct quantities
    print(1 - pieces[0], 1 - pieces[1], 2 - pieces[2], 2 - pieces[3], 2 - pieces[4], 8 - pieces[5])

if __name__ == "__main__":
    main()
