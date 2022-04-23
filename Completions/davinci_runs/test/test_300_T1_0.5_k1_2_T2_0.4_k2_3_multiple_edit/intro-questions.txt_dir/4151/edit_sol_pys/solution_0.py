

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    assert 2 <= n <= 2 * 10 ** 5
    assert len(a) == n
    assert all(1 <= x <= 10 ** 9 for x in a), a

    # TODO: solve the problem


if __name__ == '__main__':
    main()
