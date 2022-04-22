# coding: utf-8

import sys

def main():
    k = int(sys.stdin.readline())
    x = 7
    i = 1
    while True:
        if x % k == 0:
            sys.stdout.write(str(i) + "\n")
            return
        x = x * 10 + 7
        i += 1

if __name__ == '__main__':
    main()
