import sys

N, A, B = map(int, sys.stdin.readline().rstrip().split())  # N: 구매할 상품의 개수, A: 상품의 가격, B: 쿠폰의 가격



def min_expense(N, A, B):  # 최소 가격을 구하는 함수
    if N * A <= B:
        return N * A
    else:
        return B


print(min_expense(N, A, B))
