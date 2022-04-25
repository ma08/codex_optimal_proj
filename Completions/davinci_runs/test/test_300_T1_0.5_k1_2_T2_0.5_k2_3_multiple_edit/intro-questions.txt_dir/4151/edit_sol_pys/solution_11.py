

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    assert 2 <= n <= 2 * 10 ** 5, "n is not in [2..2*10**5]"
    assert len(a) == n, "Wrong number of elements"
    assert all(1 <= x <= 10 ** 9 for x in a), "All elements are not in [1..10**9]"

    # TODO: solve the problem


if __name__ == '__main__':
    main()
