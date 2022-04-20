
import sys

    """
    >>> min_moves([1, 2, 3], 1)
    0
    >>> min_moves([1, 2, 3], 2)
    1
    >>> min_moves([1, 2, 3], 3)
    2
    >>> min_moves([1, 2, 3], 4)
    3
    >>> min_moves([1, 2, 3], 5)
    3
    >>> min_moves([1, 2, 3], 6)
    3
    >>> min_moves([1, 2, 3], 7)
    3
    >>> min_moves([1, 2, 3], 8)
    3
    >>> min_moves([1, 2, 3], 9)
    3
    >>> min_moves([1, 2, 3], 10)
    3
    >>> min_moves([1, 2, 3], 11)
    3
    >>> min_moves([1, 2, 3], 12)
    3
    >>> min_moves([1, 2, 3], 13)
    3
    >>> min_moves([1, 2, 3], 14)
    3
    >>> min_moves([1, 2, 3], 15)
    3
    >>> min_moves([1, 2, 3], 16)
    3
    >>> min_moves([1, 2, 3], 17)
    3
    >>> min_moves([1, 2, 3], 18)
    3
    >>> min_moves([1, 2, 3], 19)
    3
    >>> min_moves([1, 2, 3], 20)
    3
    >>> min_moves([1, 2, 3], 21)
    3
    >>> min_moves([1, 2, 3], 22)
    3
    >>> min_moves([1, 2, 3], 23)
    3
    >>> min_moves([1, 2, 3], 24)
    3
    >>> min_moves([1, 2, 3], 25)
    3
    >>> min_moves([1, 2, 3], 26)
    3
    >>> min_moves([1, 2, 3], 27)
    3
    >>> min_moves([1, 2, 3], 28)
    3
    >>> min_moves([1, 2, 3], 29)
    3
    >>> min_moves([1, 2, 3], 30)
    3
    >>> min_moves([1, 2, 3], 31)
    3
    >>> min_moves([1, 2, 3], 32)
    3
    >>> min_moves([1, 2, 3], 33)
    3
    >>> min_moves([1, 2, 3], 34)
    3
    >>> min_moves([1, 2, 3], 35)
    3
    >>> min_moves([1, 2, 3], 36)
    3
    >>> min_moves([1, 2, 3], 37)
    3
    >>> min_moves([1, 2, 3], 38)
    3
    >>> min_moves([1, 2, 3], 39)
    3
    >>> min_moves([1, 2, 3], 40)
    3
    >>> min_moves([1, 2, 3], 41)
    3
    >>> min_moves([1, 2, 3], 42)
    3
    >>> min_moves([1, 2, 3], 43)
    3
    >>> min_moves([1, 2, 3], 44)
    3
    >>> min_moves([1, 2, 3], 45)
    3
    >>> min_moves([1, 2, 3], 46)
    3
    >>> min_moves([1, 2, 3], 47)
    3
    >>> min_moves([1, 2, 3], 48)
    3
    >>> min_moves([1, 2, 3], 49)
    3
    >>> min_moves([1, 2, 3], 50)
    3
    >>> min_moves([1, 2, 3], 51)
    3
    >>> min_moves([1, 2, 3], 52)
    3
    >>> min_moves([1, 2, 3], 53)
    3
    >>> min_moves([1, 2, 3], 54)
    3
    >>> min_moves([1, 2, 3], 55)
    3
    >>> min_moves([1, 2, 3], 56)
    3
    >>> min_moves([1, 2, 3], 57)
    3
    >>> min_moves([1, 2, 3], 58)
    3
    >>> min_moves([1, 2, 3], 59)
    3
    >>> min_moves([1, 2, 3], 60)
    3
    >>> min_moves([1, 2, 3], 61)
    3
    >>> min_moves([1, 2, 3], 62)
    3
    >>> min_moves([1, 2, 3], 63)
    3
    >>> min_moves([1, 2, 3], 64)
    3
    >>> min_moves([1, 2, 3], 65)
    3
    >>> min_moves([1, 2, 3], 66)
    3
    >>> min_moves([1, 2, 3], 67)
    3
    >>> min_moves([1, 2, 3], 68)
    3
    >>> min_moves([1, 2, 3], 69)
    3
    >>> min_moves([1, 2, 3], 70)
    3
    >>> min_moves([1, 2, 3], 71)
    3
    >>> min_moves([1, 2, 3], 72)
    3
    >>> min_moves([1, 2, 3], 73)
    3
    >>> min_moves([1, 2, 3], 74)
    3
    >>> min_moves([1, 2, 3], 75)
    3
    >>> min_moves([1, 2, 3], 76)
    3
    >>> min_moves([1, 2, 3], 77)
    3
    >>> min_moves([1, 2, 3], 78)
    3
    >>> min_moves([1, 2, 3], 79)
    3
    >>> min_moves([1, 2, 3], 80)
    3
    >>> min_moves([1, 2, 3], 81)
    3
    >>> min_moves([1, 2, 3], 82)
    3
    >>> min_moves([1, 2, 3], 83)
    3
    >>> min_moves([1, 2, 3], 84)
    3
    >>> min_moves([1, 2, 3], 85)
    3
    >>> min_moves([1, 2, 3], 86)
    3
    >>> min_moves([1, 2, 3], 87)
    3
    >>> min_moves([1, 2, 3], 88)
    3
    >>> min_moves([1, 2, 3], 89)
    3
    >>> min_moves([1, 2, 3], 90)
    3
    >>> min_moves([1, 2, 3], 91)
    3
    >>> min_moves([1, 2, 3], 92)
    3
    >>> min_moves([1, 2, 3], 93)
    3
    >>> min_moves([1, 2, 3], 94)
    3
    >>> min_moves([1, 2, 3], 95)
    3
    >>> min_moves([1, 2, 3], 96)
    3
    >>> min_m
def min_moves(a, k):
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
        moves += len(a) - k
    return moves

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(min_moves(a, k))

if __name__ == '__main__':
    main()
