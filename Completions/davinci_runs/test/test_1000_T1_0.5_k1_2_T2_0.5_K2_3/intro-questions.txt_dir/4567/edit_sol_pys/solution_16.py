import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    a = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    a.sort(reverse=True)
    if a[0] >= 10:
        print(a[0])
    elif a[0] + a[1] >= 10:
        print(a[0] + a[1])
    else:
        print(a[0] + a[1] + a[2])


if __name__ == '__main__':
    main()
