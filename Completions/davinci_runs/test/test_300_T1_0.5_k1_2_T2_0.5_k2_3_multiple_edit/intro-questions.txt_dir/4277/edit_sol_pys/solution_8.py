
import sys
N, A, B = map(int, sys.stdin.readline().rstrip().split())


def min_expense(N, A, B, count):
    if N <= 0:
        return count


    if N % 2 == 0:
        return min_expense(N//2, A, B, count+1)

    if N % 2 == 1:
        return min_expense(N-1, A, B, count+1)


print(min_expense(N, A, B, 0))
