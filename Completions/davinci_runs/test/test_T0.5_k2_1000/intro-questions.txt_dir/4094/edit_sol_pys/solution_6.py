#!/usr/bin/env python3

import sys

def main():
    k = int(sys.stdin.readline().strip())
    i = 1
    while True:
        if not (7 * (10 ** i) - 7) % k: # 7 * 10^i - 7 = 7 * (10^i - 1)
            print(i + 1)
            break
        i += 1

if __name__ == '__main__':
    main()
