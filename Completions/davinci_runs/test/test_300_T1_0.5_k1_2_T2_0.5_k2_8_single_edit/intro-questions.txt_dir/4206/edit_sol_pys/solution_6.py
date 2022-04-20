

import sys

def main():
    # read the input
    s = sys.stdin.readline()
    s = s.strip()
    s = int(s)
    print(s)

    # convert s to a string
    s = str(s)
    print(s)

    # split the string into a list of characters
    s = list(s)
    print(s)

    # convert the list of characters to a list of integers
    s = list(map(int, s))
    print(s)

    # sum the digits in s
    s = sum(s)
    print(s)

    # if the sum is divisible by 3, s is divisible by 3
    if s % 3 == 0:
        print(len(s) - 1 )
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()
