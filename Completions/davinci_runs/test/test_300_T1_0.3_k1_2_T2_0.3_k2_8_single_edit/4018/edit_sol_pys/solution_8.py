
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(max(0, n - k))

if __name__ == '__main__':
    main()
