#!/usr/bin/env python3

# https://atcoder.jp/contests/abc039/submissions/17016764


import sys

def main():
    n = int(input())
    b = list(map(int, input().split()))

    a = []

    for i in range(n-1):
        if b[i] <= b[i+1]:
            a.append(b[i])
        else:
            a.append(b[i+1])

    a.append(b[n-2])

    print(sum(a))

if __name__ == '__main__':
    main()
