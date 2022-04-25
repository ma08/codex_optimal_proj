
import sys

def min_moves(a, k):
    a.sort()
    moves = 0
    i = 0
    j = len(a) - 1
    while i < j and moves < k:
        if a[i] == a[j]:
            moves += 1
            i += 1
        elif a[i] + 1 < a[j] and moves + 2 < k:
            a[i] += 1
            a[j] -= 1
            moves += 1
        else:
            i += 1
            j -= 1
    if len(set(a)) > 1:
        moves += len(a) - k
    return moves

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(min_moves(a, k))

if __name__ == '__main__':
    main()
