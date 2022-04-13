
import sys

def get_max_cost(n, m):
    return sum(i for i in range(1, m + 1)) + (n - m) * m - 1

def main():
    n, m = map(int, sys.stdin.readline().split())
    if n < m:
        n, m = m, n
    print(get_max_cost(n, m))

if __name__ == '__main__':
    main()
