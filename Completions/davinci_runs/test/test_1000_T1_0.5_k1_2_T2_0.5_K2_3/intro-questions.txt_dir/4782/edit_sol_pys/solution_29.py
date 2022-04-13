
import sys

def get_max_cost(n, m):
    return sum(i for i in range(1, m)) + (n - m) * m

def main():
    n, m = map(int, sys.stdin.readline().split())
    print(get_max_cost(n, m))

if __name__ == '__main__':
    main()
