
def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]][0] += 1
        else:
            d[a[i]] = [1, i]
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    mod = 998244353
    ans = 1
    for i in range(len(d)):
        if i == 0:
            ans = (ans * pow(2, d[i][0][0], mod)) % mod
        else:
            ans = (ans * d[i][0][0]) % mod
    print(ans)


if __name__ == "__main__":
    main()
