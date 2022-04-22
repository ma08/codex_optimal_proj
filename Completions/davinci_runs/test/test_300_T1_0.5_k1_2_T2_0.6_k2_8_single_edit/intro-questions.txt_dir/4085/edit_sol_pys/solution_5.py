

"""
    Author: Shihao Wang

    https://www.codechef.com/problems/DIVSUM
    Date: 2020-10-17
"""


def solve(n, divisors):
    if n == 1:
        return divisors[0] * 2 - 2
    elif n == 2:
        return divisors[0] * divisors[1]

    divisors = sorted(divisors, reverse=True)
    print(divisors)
    ans = (divisors[0] - 1) * 2
    for i in range(1, n):
        ans *= divisors[i]

    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        print(solve(n, divisors))
