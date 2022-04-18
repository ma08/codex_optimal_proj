
import math


def solve(A, B):
    print(A * B // math.gcd(A, B))  # 最小公倍数


if __name__ == '__main__':
    A, B = map(int, input().split())
    solve(A, B)
