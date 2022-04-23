
import sys

n = int(input())
v = list(map(int, input().split()))

a = [0] * (10 ** 5 + 1)  # 同じ数字が何回出現したかを保存するリスト
for i in v:
    a[i] += 1

a.sort()

ans = 0
if a[-1] == a[-2]:
    ans = 0
else:
    ans = a[-1] - a[-2]

print(ans)
