
import sys

def main():
    print(solve(int(sys.stdin.readline())))

def solve(n):
    if n % 2 == 0:
        return n // 2 - 1
    else:
        return n // 2

if __name__ == '__main__':
    main()
