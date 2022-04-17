

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)[0]
    mod = 998244353
    ans = 1
    ans = (ans * pow(2, d[1], mod)) % mod
    print(ans)


if __name__ == "__main__":
    main()
