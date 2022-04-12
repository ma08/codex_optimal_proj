
from copy import deepcopy
import sys

N, A, B, C = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(N):
    l.append(int(sys.stdin.readline()))

l.sort()

def dfs(l, a, b, c, mp, cnt):
    if mp < 0 or (a > A or b > B or c > C): # mpがマイナスになったら終了
        return float('inf')
    if a == A and b == B and c == C: # 全ての材料が揃ったら終了
        return cnt
    if len(l) == 0: # 材料がなくなったら終了
        return float('inf')
    if l[0] >= 2 and mp >= 0: # 材料を2つにする
        l[0] -= 2
        ans = min(ans, dfs(l, a, b, c, mp-1, cnt+1))
        l[0] += 2
    if a < A: # 材料をAに入れる
        ans = min(ans, dfs(l, a+l[0], b, c, mp-(A-a), cnt))
    if b < B: # 材料をBに入れる
        ans = min(ans, dfs(l, a, b+l[0], c, mp-(B-b), cnt))
    if c < C: # 材料をCに入れる
        ans = min(ans, dfs(l, a, b, c+l[0], mp-(C-c), cnt))
    if mp >= 0: # 材料を捨てる
        ans = min(ans, dfs(l[1:], a, b, c, mp-9, cnt+9))
    return ans # 最小値を返す

print(dfs(l, 0, 0, 0, 100))
