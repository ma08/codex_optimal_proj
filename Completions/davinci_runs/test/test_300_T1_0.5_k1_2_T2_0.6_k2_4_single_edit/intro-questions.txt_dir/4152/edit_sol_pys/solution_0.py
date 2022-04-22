
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:23:18 2019

@author: tushar
"""

def solve(arr):
    memo = [False] * (2 ** 20)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] < 2 ** 20:
                memo[arr[i] + arr[j]] = True
    return len(arr) - sum(memo)

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solve(arr))


if __name__ == "__main__":
    main()
