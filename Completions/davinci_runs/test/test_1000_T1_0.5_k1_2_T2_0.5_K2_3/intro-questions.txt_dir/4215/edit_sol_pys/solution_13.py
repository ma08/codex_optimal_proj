import sys
input = sys.stdin.readline


def main():
    A, B = map(int, input().rstrip().split())

    print(A - B)

if __name__ == '__main__':
    main()
