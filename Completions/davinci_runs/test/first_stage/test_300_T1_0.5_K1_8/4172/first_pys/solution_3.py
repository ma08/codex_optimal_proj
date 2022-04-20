

import sys

def get_min_moves(n, k, a):
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a:
        return 0
    if n == k:
        return max_a-min_a
    min_moves = sys.maxsize
    for i in range(min_a, max_a+1):
        moves = 0
        for j in range(n):
            if a[j] > i:
                moves += a[j]-i
            else:
                moves += i-a[j]
        if moves < min_moves:
            min_moves = moves
    return min_moves


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(get_min_moves(n, k, a))