

import sys

def main():
    # read the input
    s = sys.stdin.readline()
    s = s.strip()
    s = int(s)
    print(s)

    # convert s to a string and print it
    s = str(s)
    #print(s)

    # split the string into a list of characters and print it
    s = list(s)
    print(s)

    # convert the list of characters to a list of integers and print it
    s = list(map(int, s))
    print(s)

    # sum the digits in s and print it
    s = sum(s)
    print(s)

    # if the sum is divisible by 3, s is divisible by 3
    if s % 3 == 0:
        print(len(s) - 1)
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()
