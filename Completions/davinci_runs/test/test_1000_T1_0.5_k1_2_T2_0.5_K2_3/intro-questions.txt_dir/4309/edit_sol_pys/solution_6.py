#!/usr/bin/python3

import sys

def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N, 1000):
        if (i % 111) == 0: # if the remainder is 0, then it is divisible by 111
            print(i)
            break

if __name__ == "__main__":
    main()
