import sys


def main():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    count = 1

    for i in range(1, n):
        if p[i-1] < p[i]:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
