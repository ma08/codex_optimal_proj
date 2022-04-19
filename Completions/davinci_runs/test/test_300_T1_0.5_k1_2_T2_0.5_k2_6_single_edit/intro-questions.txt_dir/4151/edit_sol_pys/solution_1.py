
import sys

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    assert 2 <= n <= 2 * 10 ** 5
    assert len(a) == n
    assert all(1 <= x <= 10 ** 9 for x in a)

    # TODO: solve the problem


if __name__ == '__main__':
    main()
