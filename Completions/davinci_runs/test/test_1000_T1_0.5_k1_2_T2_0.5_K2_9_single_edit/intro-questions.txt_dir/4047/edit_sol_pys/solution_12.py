import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())




n = int(input())
x = list(map(int, input().split()))

# x = [1, 2, 3]
# n = 3

x.sort()

min_cost = float('inf')
for i in range(n):
    cost = 0  # 初期化
    for j in range(n):  # 各点への移動距離を計算
        cost += abs(x[j] - x[i])  # 初期点からの移動距離を計算
    min_cost = min(min_cost, cost)  # 最小値を更新

print(min_cost)
