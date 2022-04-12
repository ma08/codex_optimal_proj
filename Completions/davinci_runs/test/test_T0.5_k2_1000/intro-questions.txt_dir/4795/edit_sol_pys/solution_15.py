#!/usr/bin/env python3

import sys

def main():
    N = int(input())

    X = 0

    for i in range(N):
        P = input()
        X += int(P[-1]) ** int(P[0])

    print(X)

if __name__ == '__main__':
    main()
