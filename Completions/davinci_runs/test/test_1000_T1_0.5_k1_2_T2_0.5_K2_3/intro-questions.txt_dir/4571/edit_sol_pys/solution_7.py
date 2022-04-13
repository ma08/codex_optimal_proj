
from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    print(n * 100 + 1900 * sum([(1 / 2) ** i for i in range(m)]))

if __name__ == '__main__':
    main()
