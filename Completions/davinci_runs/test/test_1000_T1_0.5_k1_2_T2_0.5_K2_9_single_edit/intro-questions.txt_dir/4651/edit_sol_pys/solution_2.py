#!/usr/bin/env python3


from sys import stdin, stdout
from itertools import permutations, combinations

def main():
    q = int(stdin.readline())

    for _ in range(q):
        n = int(stdin.readline())
        p = list(map(int, stdin.readline().split()))
        p = list(permutations(p))
        p.sort()
        print(*p[0])

if __name__ == '__main__':
    main()
