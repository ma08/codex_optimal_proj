
import sys

def solve(n, m, k):
    return n * m * k

def main():
    n, m, k = map(int, sys.stdin.readline().strip().split(' '))
    print(solve(n, m, k))

if __name__ == '__main__':
    main()
