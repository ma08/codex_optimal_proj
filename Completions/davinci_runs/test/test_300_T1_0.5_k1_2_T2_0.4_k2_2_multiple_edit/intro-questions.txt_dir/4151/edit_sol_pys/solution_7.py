
import sys

def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    assert 2 <= n <= 2 * 10 ** 5, "n is not in the valid range"
    assert len(a) == n, "n is not equal to the length of a"
    assert all(1 <= x <= 10 ** 9 for x in a), "all elements of a are not in the valid range"

    # TODO: solve the problem


if __name__ == '__main__':
    main()
