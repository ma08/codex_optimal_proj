

# Solution to https://www.hackerrank.com/challenges/circular-array-rotation

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        m = int(input())
        print(a[(n-k%n+m)%n])

if __name__ == "__main__":
    main()
