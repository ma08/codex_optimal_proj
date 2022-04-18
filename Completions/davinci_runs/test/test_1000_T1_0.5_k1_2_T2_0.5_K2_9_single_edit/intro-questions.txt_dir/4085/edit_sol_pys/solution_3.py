

"""
    Author: Shihao Wang
    Date: 2020-10-17
"""


def solve(n, divisors):
    if n == 1:
        return divisors[0] * 2
    elif n == 2:
        return divisors[0] * divisors[1]
    else:
        return -1


if __name__ == "__main__":
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # number of divisors
        divisors = list(map(int, input().split()))  # list of divisors
        print(solve(n, divisors))
