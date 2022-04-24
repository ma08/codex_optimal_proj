

import sys

def main():
    # read the input
    n = sys.stdin.readline()
    n = n.strip()
    n = int(n)
    #print(s)

    # convert s to a string
    s = str(n)
    #print(s)

    # split the string into a list of characters
    s = list(s)
    #print(s)

    # convert the list of characters to a list of integers
    s = list(map(int, s))
    #print(s)

    # sum the digits in s
    s = sum(s)
    #print(s)

    # if the sum is divisible by 3, s is divisible by 3, otherwise it's not
    if s % 3 == 0:
        print(len(str(n)) - 1)
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()
