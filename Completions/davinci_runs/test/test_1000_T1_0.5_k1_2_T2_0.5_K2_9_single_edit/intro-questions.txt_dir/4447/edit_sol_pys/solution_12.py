

from sys import stdin
from math import gcd

def main():
    n, m = (int(x) for x in stdin.readline().split())
    a = [int(x) for x in stdin.readline().split()]
    a.sort()
    min_val = a[0]
    max_val = a[-1]
    max_moves = max_val - min_val
    min_moves = 0
    for i in range(1, n):
        if i % m == 0:
            min_moves += a[i-1] - min_val
    if min_moves > max_moves:
        print(min_moves)
        for i in range(n):
            if i % m == 0:
                print(max_val, end=' ')
            else:
                print(min_val, end=' ')
    else:
        print(max_moves)
        for i in range(n):
            if i % m == 0:
                print(min_val, end=' ')
            else:
                print(max_val, end=' ')

main()
