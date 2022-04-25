

def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    mod = 998244353
    ans = 1
    for i in range(len(d)):
        if i == 0:
            ans = (ans * modpow(2, d[i][1]-1, mod)) % mod
        else:
            ans = (ans * d[i][1]) % mod
    print(ans)


if __name__ == "__main__":
    main()
