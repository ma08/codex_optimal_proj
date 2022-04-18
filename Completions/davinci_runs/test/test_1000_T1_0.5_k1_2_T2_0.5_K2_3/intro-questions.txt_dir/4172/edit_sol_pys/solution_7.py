

import sys

def min_moves(a, m):
    a.sort()
    moves = 0
    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] == a[i + 1]:
            i += 1
        elif a[j] == a[j - 1]:
            j -= 1
        elif a[i] + 1 < a[j]:
            a[i] += 1
            a[j] -= 1
            moves += 1
        else:
            i += 1
            j -= 1
    if len(set(a)) > 1:
        moves += len(a) - m
    return moves

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(min_moves(a, m))

if __name__ == '__main__':
    main()
