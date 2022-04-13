def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort(reverse=True)
    ans = 0
    for i in range(m):
        if a[i] < b[i]:
            ans += b[i]
        else:
            ans += a[i]
    print(ans)


if __name__ == "__main__":
    main()
