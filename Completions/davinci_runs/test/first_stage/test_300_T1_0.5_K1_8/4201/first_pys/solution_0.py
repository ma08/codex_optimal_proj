

from itertools import combinations

H, W, K = map(int, input().split())

c = [input() for _ in range(H)]

ans = 0

for i in range(H+1):
    for j in combinations(range(W), i):
        for k in range(H+1):
            for l in combinations(range(W), k):
                x = 0
                for m in range(H):
                    for n in range(W):
                        if m in l or n in j:
                            if c[m][n] == '#':
                                x += 1
                if x == K:
                    ans += 1

print(ans)