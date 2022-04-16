
def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for ai in a:
        d[ai] = d.get(ai, 0) + 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    mod = 998244353
    ans = 1
    for d_ in d:
        if d_[0] == 0:
            ans = (ans * pow(2, d_[1], mod)) % mod
        else:
            ans = (ans * d_[1]) % mod
    print(ans)


if __name__ == "__main__":
    main()
