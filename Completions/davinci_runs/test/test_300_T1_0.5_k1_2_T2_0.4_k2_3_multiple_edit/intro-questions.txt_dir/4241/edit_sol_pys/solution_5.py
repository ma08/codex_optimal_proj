import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()




S = input()
T = input()

ans = len(S)
for i in range(len(S)-len(T)+1):
    count = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            count += 1
    ans = min(ans, count)

print(ans)

# 文字列の部分文字列を求める問題では，横方向のループを縦方向のループとすることで，効率的に解くことができる．（この問題ではこれができない）
