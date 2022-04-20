from collections import deque
from itertools import permutations


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 全探索
ans = 0
for p in permutations(a):
    # 入れ替えた料理と満足度を保存
    d = deque(zip(p, b))
    total = 0
    while d:
        # 取り出した料理と満足度
        x, y = d.popleft()
        # 直前に食べた料理と同じものを食べたときのポイントを減算する
        if d and d[0][0] == x:
            d.popleft()
            total += y
        # 合計を計算
        total += y
    ans = max(ans, total)

# 合計を計算
total = sum(B) + sum(C)

# 直前に食べた料理と同じものを食べたときのポイントを減算する
for i in range(N-2):
    if order_A[i] == order_A[i+1]:
        total -= C[i]

print(total)
