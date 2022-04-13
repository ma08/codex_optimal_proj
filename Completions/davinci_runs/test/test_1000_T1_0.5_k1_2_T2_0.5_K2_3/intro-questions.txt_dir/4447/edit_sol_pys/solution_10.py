
from sys import stdin

def read():
    return stdin.readline()


def main():
    n, m = map(int, read().split())
    a = list(map(int, read().split()))
    print(min(max(a) - m, max(a) - min(a) - 2 * (m - 1)))

main()
