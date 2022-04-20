

import sys
import math

def solve(s, b):
    #print(s, b)
    n = len(s)
    if n == 1:
        return s
    if n == 2:
        if b[0] == 0 and b[1] == 0:
            return s
        elif b[0] == 1 and b[1] == 1:
            return s[::-1]
        else:
            return None
    b1 = b[:n//2]
    b2 = b[n//2:]
    s1 = s[:n//2]
    s2 = s[n//2:]
    s12 = s1 + s2
    c = 0
    for i in range(n//2):
        c += sum(1 for j in range(n//2, n) if s12[j] > s12[i])
    if c != sum(b1):
        return None
    s21 = s2 + s1
    c = 0
    for i in range(n//2, n):
        c += sum(1 for j in range(n//2) if s21[j] > s21[i])
    if c != sum(b2):
        return None
    s1 = solve(s1, b1)
    s2 = solve(s2, b2)
    if s1 is None or s2 is None:
        return None
    return s1 + s2

def main():
    q = int(input())
    for i in range(q):
        s = input()
        n = int(input())
        b = list(map(int, input().split()))
        s = solve(s, b)
        if s is None:
            print("-1")
        else:
            print(s)

if __name__ == "__main__":
    main()