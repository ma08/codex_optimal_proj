# coding: utf-8

n, k = map(int, input().split())
s = input()

ans = 0

for i in range(n):
    if s[i] == '1':
        continue
    if i - k >= 0 and s[i - k] == '1':  # 左隣が1なら飛ばす
        continue
    if i + k < n and s[i + k] == '1':  # 右隣が1なら飛ばす
        continue
    ans += i + 1

print(ans)
