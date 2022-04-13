

"""
    Author: Shihao Wang
    Date: 2020-10-17
"""


def solve(n, divisors):
    return divisors[0] * divisors[1] ** 2


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        print(solve(n, divisors))
