#!/usr/bin/env python3

import sys

def main():
    N = int(sys.stdin.readline().strip())
    if N > 1000:
        print(1000)
    else:
        for i in range(N, 1000):
            if (i % 111) == 0:
                print(i)
                break

if __name__ == "__main__":
    main()
