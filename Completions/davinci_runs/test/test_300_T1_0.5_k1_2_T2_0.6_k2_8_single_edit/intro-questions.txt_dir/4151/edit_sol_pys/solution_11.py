import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))[:n]
    assert 2 <= n <= 2 * 10**5
    assert all(1 <= x <= 10**9 for x in a)

    # print(n, m, a)


if __name__ == '__main__':
    main()
