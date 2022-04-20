
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    if n % k == 0:
        print(0)
    else:
        print(n % k)

if __name__ == '__main__':
    main()
