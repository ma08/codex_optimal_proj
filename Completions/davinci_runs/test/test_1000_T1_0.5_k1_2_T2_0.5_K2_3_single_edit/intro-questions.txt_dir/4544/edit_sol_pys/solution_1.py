

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# 要素数をカウントし、最も多い要素を探す
count = {}
for i in range(n):
    if a[i] in count:
        count[a[i]] += 1
    else:
        count[a[i]] = 1

# 要素の最大値を求める
max_value = 0
for key in count.keys():
    if count[key] > max_value:
        max_value = count[key]

# 要素の最大値を持つ要素の中で最小の要素を探す
max_key = 0
for key in count.keys():
    if count[key] == max_value:
        max_key = key

# 要素の最大値を持つ要素以外の要素を探す
min_key = max_key
for key in count.keys():
    if count[key] != max_value:
        if key < min_key:
            min_key = key

# 要素の最大値を持つ要素以外の要素が1つしかない場合、その要素を最小値にする
if len(count) == 2:
    min_key = max_key - 1

# 要素の最大値を持つ要素以外の要素を最小値にする
for i in range(n):
    if a[i] != max_key:
        a[i] = min_key

# 要素の最大値を持つ要素を最大値にする
for i in range(n):
    if a[i] == max_key:
        a[i] = max_value

# 要素の最大値を持つ要素の数をカウントする
count = 0
for i in range(n):
    if a[i] == max_value:
        count += 1

print(count)
