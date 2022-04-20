"""
    問題文
    入力された整数 N の桁数が奇数の整数の数を出力してください。

    制約
    1≤N≤10^9
    入力はすべて整数である。
"""

import math

N = int(input())

ans = 0

for i in range(1, N+1):
    if math.log10(i)+1 % 2 == 1:
        ans += 1

print(ans)
