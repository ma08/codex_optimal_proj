
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.buffer.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
from functools import partial

N, K = map(int, input().split())

A = [0] * K
for i in range(K):
    d = int(input())
    A[i] = list(map(int, input().split()))

A_flat = [] * K
for i in range(K):  # A[i]に含まれる数字をリストA_flatに入れる
    A_flat.extend(A[i])  # extendはリストを結合する
A_flat = set(A_flat)

ans = N - len(A_flat)
print(ans)
