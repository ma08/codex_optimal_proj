

def comb(n, r, mod=10**9+7):
    r = min(n-r, r)
    if r == 0:
        return 1
    numer = 1
    denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = []
    for i in range(n):
        d.append(a[i])
    d = sorted(d)
    print(d)
    cnt = 1
    prev = d[0]
    for i in range(1, len(d)):
        if d[i] == prev:
            cnt += 1
        else:
            print(cnt)
            cnt = 1
            prev = d[i]
    print(cnt)


if __name__ == "__main__":
    main()
