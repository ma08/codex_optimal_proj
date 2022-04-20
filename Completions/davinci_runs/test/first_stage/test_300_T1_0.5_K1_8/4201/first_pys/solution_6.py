

from itertools import combinations

H, W, K = map(int, input().split())

grid = [input().split() for _ in range(H)]

# 列挙
n_list = []
for i in range(H+1):
    for j in range(W+1):
        if i*W + j*H - 2*i*j == K:
            n_list.append((i,j))

# 列挙したものを元に探索
ans = 0
for n in n_list:
    ans += len(list(combinations(range(H), n[0]))) * len(list(combinations(range(W), n[1])))

print(ans)