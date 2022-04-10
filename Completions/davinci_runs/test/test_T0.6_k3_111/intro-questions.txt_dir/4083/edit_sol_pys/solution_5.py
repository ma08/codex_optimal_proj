
def main():
    n, k = map(int, input().split())
    a = map(int, input().split())
    a.sort()
    diff = a[n - 1] - a[0]
    while diff > 0:
        a[0] += 1
        a[n - 1] -= 1
        a.sort()
        diff = a[n - 1] - a[0]
    print a[n - 1] - a[0]


if __name__ == '__main__':
    main()
