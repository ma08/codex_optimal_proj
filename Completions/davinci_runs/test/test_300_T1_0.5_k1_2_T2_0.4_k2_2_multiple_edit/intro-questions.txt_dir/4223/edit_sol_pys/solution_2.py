# 入力
from collections import Counter

n = int(input())
s = input()
# 文字列をカウント
c = Counter(s)
# 全ての文字をカウントした値から、文字列の長さを引く
ans = n - sum(c.values())

print(ans)
