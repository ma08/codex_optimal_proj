import math


def main():
    l, r = map(int, input().split())

    if r - l >= 2019:
        print(0)
        exit()

    mn = 2020
    for i in range(l, r):
        for j in range(i+1, r+1):
            mn = min(mn, i*j % 2019)

    print(mn)


if __name__ == "__main__":
    main()
