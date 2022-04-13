
import itertools
import collections
import random

N = int(input())
A = list(map(int, input().split()))  # 各モンスターの体力

# 各モンスターの体力をキー、各モンスターの攻撃回数を値とする辞書
attack_num = collections.defaultdict(int)

while len(attack_num) > 1:
    # 攻撃するモンスターを選択
    attacker = random.choice(monsters)
    # 攻撃されるモンスターを選択
    defender = random.choice(monsters)

    # 攻撃と防御が同じモンスターであった場合、攻撃を繰り返す
    while attacker == defender:
        defender = random.choice(monsters)

    # 攻撃するモンスターの攻撃回数をインクリメントする
    attack_num[attacker-1] += 1

    # 攻撃されるモンスターの体力を減らす
    health[defender-1] -= health[attacker-1]

    # 攻撃されるモンスターの体力が0以下になった場合
    if health[defender-1] <= 0:
        # 攻撃されるモンスターを死亡にする
        alive[defender-1] = False
        # 生きているモンスターの数をデクリメント
        alive_num -= 1

    # 攻撃を行った回数をインクリメントする
    attack_count += 1

# 最後に生き残ったモンスターの体力を出力
for i in range(n):
    if alive[i]:
        print(health[i])
