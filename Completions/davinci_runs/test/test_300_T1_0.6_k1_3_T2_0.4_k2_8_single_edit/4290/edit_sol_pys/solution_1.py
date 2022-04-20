
import sys


def solve(n, m):

    return n * m

def main():
    lines = sys.stdin.readlines()
    n, m = map(int, lines[0].strip().split())

def test_solve():
    assert solve(2, 3) == 6
    assert solve(100, 100) == 10000
    print(solve(n,m))


if __name__ == '__main__':
    main()
