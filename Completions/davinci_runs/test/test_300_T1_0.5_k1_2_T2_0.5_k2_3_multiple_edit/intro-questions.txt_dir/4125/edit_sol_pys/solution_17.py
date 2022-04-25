def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += a[i]
        else:
            ans -= a[i]

    for i in range(N):
        if i % 2 == 0:
            print(ans, end=" ")
        else:
            print(-ans, end=" ")


if __name__ == "__main__":
    main()

ans = 0
