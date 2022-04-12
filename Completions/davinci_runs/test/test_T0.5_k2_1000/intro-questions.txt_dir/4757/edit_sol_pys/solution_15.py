#!/usr/bin/python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    e = int(sys.stdin.readline().strip())
    songs = set()
    for i in range(e):
        line = sys.stdin.readline().strip().split()
        k = int(line[0])
        for j in range(k):
            songs.add(line[j + 1])
    for i in range(1, n + 1):
        print(i)

main()
