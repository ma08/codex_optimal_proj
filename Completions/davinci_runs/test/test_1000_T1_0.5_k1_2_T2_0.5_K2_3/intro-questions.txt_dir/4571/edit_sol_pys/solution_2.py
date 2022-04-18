
from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    print(n * 100 + 1900 * sum([(1 / 2.0) ** i for i in range(1, m + 1)]))

if __name__ == '__main__':
    main()
