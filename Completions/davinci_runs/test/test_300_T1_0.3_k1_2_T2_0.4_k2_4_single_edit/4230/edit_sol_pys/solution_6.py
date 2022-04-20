# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a_score = 0
    for i in range(n):
        a_score += b[a[i]-1]
        if i != n-1 and a[i] == a[i+1] - 1:
            a_score += c[a[i]-1]
    print(a_score)

if __name__ == '__main__':
    main()
