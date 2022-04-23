import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7

import math

H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
dp = [[f_inf] * W for _ in range(H)]
