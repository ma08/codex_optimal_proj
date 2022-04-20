

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    print(min(a+b, 2*(a+b-max(a, b))))


if __name__ == "__main__":
    main()