

from collections import defaultdict

def happiness(x):
    n = [500, 100, 50, 10, 5, 1] # 金種ごとに紙幣の枚数を管理するリスト
    d = defaultdict(int)
    for i in range(len(n)): # 金種ごとに紙幣の枚数を管理するリストの要素数分ループ
        d[n[i]] = x // n[i] # 金種ごとに紙幣の枚数を管理するリストの要素に対して、紙幣の枚数を計算
        x %= n[i] # 残りの金額を計算
    return 1000 * d[500] + 5 * d[5] # 紙幣の枚数を計算したリストから、紙幣の枚数を計算

x = int(input())
print(happiness(x))
