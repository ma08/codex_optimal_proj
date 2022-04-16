
# -*- coding: utf-8 -*-

from sys import stdin

def main():
    n = int(stdin.readline())
    line = list(map(int, stdin.readline().split()))
    line.sort()
    if n % 2 == 0:
        line.reverse()
    print(" ".join([str(x) for x in line]))

if __name__ == "__main__":
    main()
