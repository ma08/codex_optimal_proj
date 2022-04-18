
import math
import sys

def min_moves(a, k):
    a = sorted(a)
    moves = 0
    i, j = 0, len(a) - 1
    while i < j and a[i] == a[i + 1]:
        i += 1
    while i < j and a[j] == a[j - 1]:
        j -= 1
    while i < j and a[i] + 1 < a[j]:
        a[i] += 1
        a[j] -= 1
        moves += 1
        while a[i] == a[i + 1]:
            i += 1
        while a[j] == a[j - 1]:
            j -= 1
    if len(set(a)) > 1:
        moves += math.ceil(len(a) / k)
    return moves

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(min_moves(a, k))

if __name__ == '__main__':
    main()
