
import math

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(min_moves(a, n))

def min_moves(a, n):
    if n % 2 == 0:
        for i in range(n):
            if i % 2 != a[i] % 2:
                moves += 1
        return int(moves / 2)
    else:
        for i in range(n):
            if i % 2 == a[i] % 2:
                moves += 1
        return int(moves / 2) + 1

def min_moves2(a, n):
    moves = 0
    for i in range(n):
        if i % 2 != a[i] % 2 and i % 2 == 0:
            moves += 1
    if moves % 2 == 0:
        return moves // 2
    else:
        return moves // 2 + 1

def min_moves3(a, n):
    moves = 0
    for i in range(n):
        if i % 2 == a[i] % 2:
            moves += 1
    if moves % 2 == 0:
        return moves // 2
    else:
        return moves // 2 + 1

if __name__ == '__main__':
    main()
