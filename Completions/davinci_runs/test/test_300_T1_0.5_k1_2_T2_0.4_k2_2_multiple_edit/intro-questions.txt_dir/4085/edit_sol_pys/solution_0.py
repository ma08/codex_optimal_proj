

"""
    Author: Shihao Wang
    Date: 2020-10-17
"""
Description:
    Given an integer n, return the product of all its divisors.
    If n has no divisors, return -1.

Example:
    Input: n = 3
    Output: -1

    Input: n = 4
    Output: 8

    Input: n = 5
    Output: -1

    Input: n = 6
    Output: 12

Solution:
    The product of all divisors of n is n * (n - 1) if n is a prime number,
    otherwise, it is -1.



def solve(n, divisors):
    if n == 1:
        return divisors[0] * 2
    elif n == 2:
        return divisors[0] * divisors[1]
    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        print(solve(n, divisors))
