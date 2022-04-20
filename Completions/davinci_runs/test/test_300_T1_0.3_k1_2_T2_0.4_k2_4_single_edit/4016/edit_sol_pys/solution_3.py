
import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    t = sys.stdin.readline().strip()
    print(t * (k // n) + t[:k % n])


if __name__ == "__main__":
    main()
