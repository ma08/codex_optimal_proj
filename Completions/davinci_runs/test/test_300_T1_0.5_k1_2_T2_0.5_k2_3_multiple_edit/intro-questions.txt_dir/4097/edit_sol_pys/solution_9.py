#!/bin/python3

import math

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = math.inf
    for i in range(n-1):
        ans = min(ans,arr[i+1]-arr[i])
    print(ans)

if __name__ == "__main__":
    main()
