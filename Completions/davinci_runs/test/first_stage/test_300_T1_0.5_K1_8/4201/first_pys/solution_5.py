

# H, W, K = map(int, input().split())
# c = [list(input()) for _ in range(H)]

H, W, K = 2, 3, 2
c = [[".", ".", "#"], ["#", "#", "#"]]

ans = 0
for i in range(2 ** H):
    for j in range(2 ** W):
        black = 0
        for k in range(H):
            for l in range(W):
                if (i >> k) & 1 or (j >> l) & 1:
                    if c[k][l] == "#":
                        black += 1
        if black == K:
            ans += 1
print(ans)