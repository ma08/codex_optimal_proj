
# ここにコードを書いてみよう

N = int(input())
L = list(map(int, input().split()))

comb = list(itertools.combinations(L, 3))

count = 0
for c in comb:
    if c[0] + c[1] > c[2] and c[1] + c[2] > c[0] and c[2] + c[0] > c[1]:
        count += 1

print(count)
