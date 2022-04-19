import sys

k, x = list(map(int, sys.stdin.readline().split()))


def main():
    for i in range(k):
        print(x - k + 1 + i, end=" ")


if __name__ == "__main__":
    main()
