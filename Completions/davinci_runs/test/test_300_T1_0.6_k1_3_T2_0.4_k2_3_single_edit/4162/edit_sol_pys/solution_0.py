import sys


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    b = [0] * _
    for i in range(_):
        for j in range(a[i]):
            b[i] += (j + 1) * (a[i] - j)
    print(sum(b))


if __name__ == '__main__':
    main()
