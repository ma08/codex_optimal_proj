

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(0 if a[0] == a[-1] else -1)
    else:
        print(0 if a[0] == a[-1] else 1 if a[0] + 1 == a[-1] else -1)


if __name__ == '__main__':
    main()
