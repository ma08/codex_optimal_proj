"""
    This is a sample file to test the git
"""


def solve(n):
    return n // 2


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))
