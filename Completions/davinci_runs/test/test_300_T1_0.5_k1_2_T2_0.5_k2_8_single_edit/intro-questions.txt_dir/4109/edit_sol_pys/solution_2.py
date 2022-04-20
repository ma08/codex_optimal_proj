

import sys

ans = 10**10
for i in range(1 << N):
    # 各書籍について、ビットが立っていると購入する、立っていないと購入しない
    # この時、各アルゴリズムについて、購入した書籍の内、各アルゴリズムのレベルが最も高いものを足し合わせる
    # これがX以上になればOK
    cost = 0
    level = [0] * M
    for j in range(N):
        # 購入する書籍
        if i & (1 << j):
            cost += C[j]
            for k in range(M):
                level[k] = max(level[k], A[j][k])
    # すべてのアルゴリズムのレベルがX以上であれば、コストの最小値を更新する
    if all(x >= X for x in level):
        ans = min(ans, cost)

# すべてのアルゴリズムのレベルがX以上になれば、コストが最小値になる
if ans == 10**10:
    print(-1)
else:
    print(ans)
