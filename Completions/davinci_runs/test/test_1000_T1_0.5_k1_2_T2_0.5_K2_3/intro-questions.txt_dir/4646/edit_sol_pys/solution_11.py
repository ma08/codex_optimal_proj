import math


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(min_moves(a, n))



def min_moves(a, n):
    if n % 2 != 0:
        return -1
    moves = 0
    for i in range(n):
        if i % 2 != a[i] % 2:
            moves += 1
    return int(moves / 2)


def min_moves_2(a):
    odd = 0
    even = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even % 2 == 0 and odd % 2 == 0:
        return 0
    elif even % 2 == 1 and odd % 2 == 1:
        return 1
    else:
        return -1


if __name__ == '__main__':
    main()
