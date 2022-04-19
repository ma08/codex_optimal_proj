import sys
import math


def main():
    n = int(input())
    a = list(map(int,sys.stdin.readline().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans = max(ans,a[i]*(n-i))
    print(ans)


if __name__ == '__main__':
    main()
