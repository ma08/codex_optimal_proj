
def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    mod = 998244353
    ans = 1
    for k, v in d.items():
        ans = (ans * pow(2, v, mod)) % mod
    print(ans)


if __name__ == "__main__":
    main()
