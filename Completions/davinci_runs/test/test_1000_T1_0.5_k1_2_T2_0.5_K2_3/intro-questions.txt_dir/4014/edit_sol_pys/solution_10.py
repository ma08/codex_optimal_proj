
def main():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))

    l = 0
    r = 0
    cost = 0
    ans = n + 1
    while True:
        if cost < x:
            if r == n:
                break
            cost += a[r]
            r += 1
        else:
            ans = min(ans, r - l)
            cost -= a[l]
            l += 1

    if ans == n + 1:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
