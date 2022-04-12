

import sys

def main():
    # Get input, and convert to int
    n = int(sys.stdin.readline())

    # Print the number of digits in n
    print(len(str(n)))

if __name__ == '__main__':
    main()
