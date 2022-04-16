


def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(min([a[i] - a[i-1] for i in range(1, n)]))


if __name__ == '__main__':
    main()
