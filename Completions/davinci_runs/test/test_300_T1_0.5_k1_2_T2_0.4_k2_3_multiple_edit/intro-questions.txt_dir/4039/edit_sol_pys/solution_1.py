#!/usr/bin/env python3

import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    projects = []
    for i in range(n):
        projects.append(list(map(int, sys.stdin.readline().split())))

    projects.sort(key=lambda x: x[1])

    for i in range(n):
        if projects[i][0] > r:
            print("NO")
            sys.exit()
        r += projects[i][1]
        if r < 0 or r > 1000000000:
            print("NO")
            sys.exit()

    print("YES")

if __name__ == '__main__':
    main()
