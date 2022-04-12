
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        print(0)
        return
    if a[0] + 1 == a[1] or a[-1] - 1 == a[-2]:
        print(a[-1] - a[1])
        return
    print(min(a[-1] - a[1], a[-2] - a[0]))


if __name__ == "__main__":
    main()
