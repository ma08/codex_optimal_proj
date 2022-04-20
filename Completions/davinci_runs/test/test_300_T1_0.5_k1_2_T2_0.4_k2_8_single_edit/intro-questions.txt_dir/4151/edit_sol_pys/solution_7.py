

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: x[0], reverse=True)
    mod = 998244353
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * pow(i, d[i - 1][1], mod)) % mod
    print(ans)


if __name__ == "__main__":
    main()
