

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split())) # a[i] is the number of apples on the i-th tree
    assert 2 <= n <= 2 * 10**5
    assert len(a) == n
    assert all(1 <= x <= 10**9 for x in a)

    # TODO: solve the problem and output the result


if __name__ == '__main__':
    main()
