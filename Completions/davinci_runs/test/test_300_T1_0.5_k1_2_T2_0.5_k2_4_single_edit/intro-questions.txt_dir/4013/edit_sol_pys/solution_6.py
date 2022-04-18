
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        print(0)
        return
    print(min(a[-1] - a[1], a[-2] - a[0]) + min(a[1] - a[0], a[-1] - a[2]))


if __name__ == "__main__":
    main()
