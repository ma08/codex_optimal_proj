

"""
    Author: Shihao Wang
    Date: 2020-10-17
"""


def solve(n, divisor):
    if n == 1:
        return divisor[0] * divisor[0]
    elif n == 2:
        return divisor[0] * divisor[1]
    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisor = list(map(int, input().split()))
        print(solve(n, divisor))
