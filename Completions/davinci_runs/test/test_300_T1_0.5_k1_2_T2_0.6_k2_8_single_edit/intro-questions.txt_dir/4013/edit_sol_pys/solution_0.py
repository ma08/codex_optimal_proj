
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        print(0)
    if a[0] + 1 == a[1]:
        print(a[-1] - a[1])
    if a[-1] - 1 == a[-2]:
        print(a[-1] - a[0])
    print(min(a[-1] - a[1], a[-2] - a[0]))


if __name__ == "__main__":
    main()
