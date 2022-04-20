

import sys

n, m = map(int, input().split())

l_r = []
for _ in range(m):
    l, r = map(int, input().split())
    l_r.append((l, r))

l_r = sorted(l_r)
print(l_r)

# 全てのゲートを通れるIDカードの候補をリストに保存
candidate_id_cards = list(range(1, n+1))
for l, r in l_r:
    for i in range(l, r+1):
        if i in candidate_id_cards:
            candidate_id_cards.remove(i)

print(len(candidate_id_cards))