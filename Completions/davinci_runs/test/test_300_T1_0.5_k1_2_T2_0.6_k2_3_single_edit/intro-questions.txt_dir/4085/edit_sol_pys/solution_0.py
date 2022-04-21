

"""
    Author: Shihao Wang
    Date: 2020-10-17
"""
    """
    :param n: length of divisors
    :param divisors: a list of divisors
    :return: the maximum area of the rectangle
    """


def solve(n, divisors):
    if n == 1:
        return divisors[0] * 2
    if n == 2:
        return divisors[0] * divisors[1]
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        print(solve(n, divisors))
