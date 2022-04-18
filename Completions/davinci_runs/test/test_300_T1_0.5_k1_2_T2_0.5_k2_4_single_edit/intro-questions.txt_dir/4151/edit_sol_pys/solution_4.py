
import math


def main():
    n = int(input())
    a = list(map(int, input().split()))  # 各数字は何回出現したか
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)  # 出現回数順にソート
    print(d)
    mod = 998244353
    ans = 1
    for i in range(1, len(d)):
        ans = (ans * math.factorial(d[i][1])) % mod
    print(ans)


if __name__ == "__main__":
    main()
