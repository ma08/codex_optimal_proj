
from math import ceil

def solve(x):
    return ceil(x/2)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x = int(input())
        print(solve(x))
