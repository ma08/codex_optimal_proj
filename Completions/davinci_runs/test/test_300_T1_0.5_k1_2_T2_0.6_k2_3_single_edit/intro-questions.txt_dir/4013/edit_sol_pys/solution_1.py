import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    a.sort()
    if n == 2:
        print(0)
        return
    if abs(a[0] - a[1]) == 1:
        print(a[-1] - a[1])
        return
    if abs(a[-1] - a[-2]) == 1:
        print(a[-1] - a[0])
        return
    print(min(a[-1] - a[1], a[-2] - a[0]) - 1)


if __name__ == "__main__":
    main()
