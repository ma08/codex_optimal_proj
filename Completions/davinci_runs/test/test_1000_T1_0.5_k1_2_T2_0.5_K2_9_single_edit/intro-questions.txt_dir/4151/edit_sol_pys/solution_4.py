

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: -x[1])
    mod = 998244353
    ans = 1
    for i, v in enumerate(d):
        if i == 0:
            ans = (ans * pow(2, v[1], mod)) % mod
        else:
            ans = (ans * v[1]) % mod
    print(ans)


if __name__ == "__main__":
    main()
