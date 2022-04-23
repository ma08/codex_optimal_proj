
import sys

def main():
    print(solve(int(sys.stdin.readline())))

def solve(n):
    return n // 2 - 1 if n % 2 == 0 else n // 2

if __name__ == '__main__':
    main()
