import sys
input = sys.stdin.readline


def main():
    A, B, T = map(int, input().strip().split())
    print(B * (T // A + 1))


if __name__ == '__main__':
    main()
