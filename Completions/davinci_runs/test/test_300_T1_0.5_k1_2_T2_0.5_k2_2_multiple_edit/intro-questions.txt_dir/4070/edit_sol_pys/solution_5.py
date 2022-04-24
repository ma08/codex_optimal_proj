
import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    print(solve(a, b))

def solve(a, b):
    if a % 2 == 0:
        return a // 2 * b
    else:
        return a // 2 * b + b // 2

if __name__ == '__main__':
    main()
