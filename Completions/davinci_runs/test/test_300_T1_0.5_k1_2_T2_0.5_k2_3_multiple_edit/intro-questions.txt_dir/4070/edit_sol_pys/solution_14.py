import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    print(solve(a, b))

def solve(a, b):
    return a + b

if __name__ == '__main__':
    main()
