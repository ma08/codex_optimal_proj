
import math


def solve(a, b, x):
    return b // x - (a - 1) // x


def main():
    a, b, x = map(int, input().split())
    print(solve(a, b, x))


def test():
    assert solve(3, 10, 3) == 3
    assert solve(4, 10, 3) == 3
    assert solve(4, 10, 5) == 2
    assert solve(4, 10, 7) == 1
    assert solve(4, 10, 10) == 1
    assert solve(4, 10, 11) == 0
    assert solve(1, 1000000000, 1) == 1000000000
    assert solve(1, 1000000000, 1000000000) == 1


if __name__ == "__main__":
    test()
    main()
