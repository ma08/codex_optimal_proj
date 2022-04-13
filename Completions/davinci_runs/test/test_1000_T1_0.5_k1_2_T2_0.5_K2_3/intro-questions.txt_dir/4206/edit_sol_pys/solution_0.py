

import sys

def main():
    # read the input
    s = sys.stdin.readline().strip()

    #print(type(s))

    # split the string into a list of characters
    s = list(s)
    #print(type(s))

    # convert the list of characters to a list of integers
    s = list(map(int, s))
    #print(type(s))

    # sum the digits in s
    s = sum(s)
    #print(type(s))

    # if the sum is divisible by 3, s is divisible by 3
    if s % 3 == 0:
        print(len(str(s)))
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()
