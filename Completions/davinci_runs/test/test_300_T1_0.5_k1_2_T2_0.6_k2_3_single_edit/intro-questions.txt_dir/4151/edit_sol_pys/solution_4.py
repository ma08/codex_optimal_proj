

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)
    mod = 998244353
    cnt = 1
    ans = 1
    for i in range(len(d)):
        if d[i][1] != d[i - 1][1]:
            cnt = 1
        ans = (ans * cnt) % mod
        cnt += 1
    print(ans)


if __name__ == "__main__":
    main()
