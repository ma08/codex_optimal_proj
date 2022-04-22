

"""
    Author: Shihao Wang, shihaowang@pku.edu.cn
    Date: 2020-10-17
"""


def solve(n, divisors):
    if n == 1 and len(divisors) == 1:
        return divisors[0] * 2
    elif n == 2 and len(divisors) == 2:
        return divisors[0] * divisors[1]
    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        divisors = list(map(int, input().split()))
        print(solve(n, divisors))
