#!/usr/bin/env python3

import sys

def main():
    k = int(sys.stdin.readline().strip()) # read integer from stdin and strip newline
    i = 1
    while True:
        if not (7 * (10 ** i) - 7) % k: # if 7 * (10 ** i) - 7 is divisible by k (7 * (10 ** i) - 7 is the smallest number that is divisible by 7 and has i digits)
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()
