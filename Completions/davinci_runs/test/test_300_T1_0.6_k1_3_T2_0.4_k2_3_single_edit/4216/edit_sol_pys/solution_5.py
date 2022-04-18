
import sys

def main():
    n = int(sys.stdin.readline())

    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())

    if a > c:
        a, b, c, d = c, d, a, b

    if b < d:
        print(0)
    else:
        print(b - d)


if __name__ == '__main__':
    main()
