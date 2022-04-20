
import sys

N, A, B = map(int, sys.stdin.readline().rstrip().split())  # N: 사람 수, A: 가격, B: 쿠폰



def min_expense(N, A, B):  # 최소 경비
    if N * A <= B:
        return N * A
    else:
        return B


print(min_expense(N, A, B))
