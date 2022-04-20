# coding: utf-8

import sys

def main():
    n, a, b, c = map(int, sys.stdin.readline().split())
    l = [int(sys.stdin.readline()) for _ in range(n)]
    l.sort()
    ans = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] < a and l[j] < b and l[k] < c:
                    ans = min(ans, (a - l[i]) + (b - l[j]) + (c - l[k]))
    print(ans)

if __name__ == '__main__':
    main()
