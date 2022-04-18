
import itertools
import random

n = int(input())
A = list(map(int, input().split()))

# 初期化
# 各モンスターの名前
monsters = list(range(1, n + 1))
# 各モンスターの体力
health = [a for a in A]
# 各モンスターの生死
alive = [True for _ in range(n)]
# 各モンスターが攻撃した回数
attack_num = [0 for _ in range(n)]

# 生きているモンスターの数
alive_num = n
# 攻撃を行った回数
attack_count = 0

while alive_num > 1:
    # 攻撃するモンスターを選択
    attacker = random.choice(monsters)
    # 攻撃されるモンスターを選択
    defender = random.choice(monsters)

    # 攻撃と防御が同じモンスターであった場合、攻撃を繰り返す
    while attacker == defender:
        defender = random.choice(monsters)

    # 攻撃するモンスターの攻撃回数をインクリメント
    attack_num[attacker - 1] += 1

    # 攻撃されるモンスターの体力を減らす
    health[defender - 1] -= health[attacker - 1]

    # 攻撃されるモンスターの体力が0以下になった場合
    if health[defender - 1] <= 0:
        # 攻撃されるモンスターを死亡にする
        alive[defender - 1] = False
        # 生きているモンスターの数をデクリメント
        alive_num -= 1

    # 攻撃を行った回数をインクリメント
    attack_count += 1

# 最後に生き残ったモンスターの体力を出力
for i in range(n):
    if alive[i]:
        print(health[i])
