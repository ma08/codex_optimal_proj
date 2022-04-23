
import bisect

def solve(a, b):
    c = [a1 + b1 for a1, b1 in zip(a, b) if a1 + b1 != 0]
    c.sort()
    return len(c)


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solve(a, b))
