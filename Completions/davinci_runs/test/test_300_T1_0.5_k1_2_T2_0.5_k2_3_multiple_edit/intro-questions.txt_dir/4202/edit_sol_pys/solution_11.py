import sys


def main():
    l, r = map(int, sys.stdin.readline().split())

    if r - l >= 2019:
        print(0)
    else:
        min_val = 2020
        for i in range(l, r):
            for j in range(i+1, r+1):
                min_val = min(min_val, (i*j) % 2019)  # noqa

        print(min_val)

if __name__ == '__main__':
    main()
