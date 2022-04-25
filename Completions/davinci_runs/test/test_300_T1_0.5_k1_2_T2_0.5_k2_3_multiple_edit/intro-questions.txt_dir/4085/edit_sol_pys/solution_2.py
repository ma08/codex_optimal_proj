

"""
    Author: Shihao Wang, Yuxin Wang, Jiahui Tang
    Date: 2020-10-17, 2020-10-18, 2020-10-19
"""


def solve(n, divisors, divisor_dict):
    if n <= 2:
        return divisors[0] * divisors[1] if n == 2 else divisors[0] * 2
    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        print(solve(n, divisors))
