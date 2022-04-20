
from math import gcd
import sys

n = int(input())
t = [int(input()) for _ in range(n)]

ans = t[0] # 最初の要素を答えとする

for i in t: # tの要素を全て試す
    ans = ans * i // gcd(ans, i) # 現在の答えにiをかける

print(ans)
