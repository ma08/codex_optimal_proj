
import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if a + b == c:
        print('Yes')
    elif a - b == c:
        print('Yes')
    elif b - a == c:
        print('Yes')
    elif a * b == c:
        print('Yes')
    elif a / b == c:
        print('Yes')
    elif b / a == c:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
