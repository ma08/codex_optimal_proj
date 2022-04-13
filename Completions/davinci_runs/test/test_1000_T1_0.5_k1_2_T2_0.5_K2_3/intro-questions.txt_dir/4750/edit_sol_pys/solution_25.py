def main():
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    if n == k:
        print(a[n-1])
    else:
        print(a[k-1])


if __name__ == "__main__":
    main()
