


def calc(n, m):
    if m == 0:
        return n * 100
    elif m == 1:
        return n * 100 + 1900
    else:
        return n * 100 + 1900 * sum([(1 / 2) ** i for i in range(1, m + 1)])
from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    print(calc(n, m))

if __name__ == '__main__':
    main()
