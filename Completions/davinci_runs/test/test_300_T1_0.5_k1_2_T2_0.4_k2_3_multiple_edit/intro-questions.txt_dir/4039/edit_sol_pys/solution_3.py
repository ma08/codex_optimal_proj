#!/usr/bin/env python3

import sys

def main():
    n, r = map(int, sys.stdin.readline().split()) # n = number of projects, r = initial rating
    projects = []
    for i in range(n):
        projects.append(list(map(int, sys.stdin.readline().split()))) # list of projects

    projects.sort(key=lambda x: x[1])

    for i in range(n):
        if projects[i][0] > r: # if rating of project is greater than current rating
            print("NO")
            sys.exit()
        r += projects[i][1] # add rating of project to current rating
        if r < 0: # if current rating is negative
            print("NO")
            sys.exit()

    print("YES")

if __name__ == '__main__':
    main()
