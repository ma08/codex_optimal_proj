import sys


def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    for i in range(1, n):
        if a[i] > a[i - 1]:
            ans += 1
    print(ans + 1)


if __name__ == "__main__":
    main()
