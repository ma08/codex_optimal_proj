#!/usr/bin/env python3

from sys import stdin

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    print(len(set(a)))

if __name__ == "__main__":
    main()
