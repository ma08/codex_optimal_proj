

import sys
from collections import Counter
from itertools import combinations

N = int(input())
S = []
for i in range(N):
    S.append(input())

# print(S)

# カウント
cnt = Counter(S)
# print(cnt)

# MARCH
cnt_march = Counter()
for s in S:
    if s[0] in ['M', 'A', 'R', 'C', 'H']:
        cnt_march[s[0]] += 1
# print(cnt_march)

# 3人組み合わせ
cnt_comb = Counter()
for k, v in cnt_march.items():
    if v >= 3:
        cnt_comb[k] += v * (v - 1) * (v - 2) // 6
    elif v == 2:
        cnt_comb[k] += v * (v - 1) // 2
    else:
        cnt_comb[k] += v
# print(cnt_comb)

# print(cnt_comb['M'] + cnt_comb['A'] + cnt_comb['R'] + cnt_comb['C'] + cnt_comb['H'])

# 3人組み合わせを作成
comb = combinations(cnt_march.keys(), 3)
# print(comb)

# MARCH以外の3人組み合わせ
cnt_comb_other = Counter()
for c in comb:
    cnt_comb_other[c] = cnt_comb[c[0]] * cnt_comb[c[1]] * cnt_comb[c[2]]
# print(cnt_comb_other)
# print(sum(cnt_comb_other.values()))

# MARCHの3人組み合わせ
cnt_comb_march = Counter()
for c in comb:
    if 'M' in c and 'A' in c and 'R' in c and 'C' in c and 'H' in c:
        cnt_comb_march[c] = cnt_comb[c[0]] * cnt_comb[c[1]] * cnt_comb[c[2]]
# print(cnt_comb_march)
# print(sum(cnt_comb_march.values()))

# MARCHの3人組み合わせを除く
print(sum(cnt_comb_other.values()) - sum(cnt_comb_march.values()))