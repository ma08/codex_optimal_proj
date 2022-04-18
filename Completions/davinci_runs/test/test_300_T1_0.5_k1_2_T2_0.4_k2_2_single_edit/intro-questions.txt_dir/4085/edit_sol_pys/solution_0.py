

"""
    Author: Shihao Wang, Yanan Zhao
    Date: 2020-10-17
"""


def solve(n, divisors):
    if n == 1:
        return divisors[0] * divisors[0]
    elif n == 2:
        return divisors[0] * divisors[1] * 2
    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        print(solve(n, divisors))
