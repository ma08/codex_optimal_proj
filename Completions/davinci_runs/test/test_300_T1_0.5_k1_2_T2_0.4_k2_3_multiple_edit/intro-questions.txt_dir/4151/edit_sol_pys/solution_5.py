
def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    d = {}  # 各数字の出現回数を記録する
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)  # 出現回数で降順にソート
    mod = 998244353
    ans = 1
    for i in range(len(d)):
        if i == 0:
            ans = (ans * pow(2, d[i][1], mod)) % mod
        else:
            ans = (ans * d[i][1]) % mod  # 最大以外の出現回数を計算
    print(ans)


if __name__ == "__main__":
    main()
