# -*- coding: utf-8 -*-


n, l = map(int, input().split())  # 入力をリストに

tastes = [l + i for i in range(n)]  # 要素を追加

print(sum(tastes) - min([abs(f) for f in tastes]))  # 要素を追加
