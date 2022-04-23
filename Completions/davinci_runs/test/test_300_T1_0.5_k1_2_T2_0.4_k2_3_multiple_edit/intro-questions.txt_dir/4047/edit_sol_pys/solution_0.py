# -*- coding: utf-8 -*-
# AtCoder Beginner Contest
 
 
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
 
    for i in range(n):
        ans += 1 / a[i]
 
    print(1 / ans)
import sys

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    if n % 2 == 0:
        print(x[n//2] - x[n//2 - 1])
    else:
        print(0)

if __name__ == "__main__":
    main()
