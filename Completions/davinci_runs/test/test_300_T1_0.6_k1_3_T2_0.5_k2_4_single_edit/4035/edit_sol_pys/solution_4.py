#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin.readlines():
        line = line.rstrip('\r\n')
        a, b = map(int, line.split())

        for i in range(1, 100):
            if int(i * 1.08) == a and int(i * 1.1) == b:
                print(i)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()
