

import math

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(min_moves(a, n))

def min_moves(a, n):
    if not n % 2:
        return -1
    moves = 0
    for i in range(n):
        if i % 2 ^ a[i] % 2:
            moves += 1
    return int(moves / 2)

if __name__ == '__main__':
    main()
