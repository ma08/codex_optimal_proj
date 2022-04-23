# https://atcoder.jp/contests/abc151/tasks/abc151_f

def main():
    n = int(input())
    a = list(map(int, input().split()))  # a[i] = i番目の要素
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1  # d[a[i]] = a[i]の個数
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)  # d[i][0] = a[i]の個数
    mod = 998244353
    ans = 1
    for i in range(len(d)):
        if i == 0:
            ans = (ans * pow(2, d[i][1], mod)) % mod  # ans = ans * 2^d[i][1]
        else:
            ans = (ans * d[i][1]) % mod  # ans = ans * d[i][1]
    print(ans)


if __name__ == "__main__":
    main()
