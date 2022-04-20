

N, M, Q = map(int, input().split())

# 入力をリストに格納
abcd = []
for i in range(Q):
    abcd.append(list(map(int, input().split())))

# 組み合わせを全探索
ans = 0
for i in range(1, M + 1):
    for j in range(i, M + 1):
        for k in range(j, M + 1):
            score = 0
            for l in range(Q):
                if (abcd[l][0] == 1 and abcd[l][1] == 2 and abcd[l][2] == i - 1) or (abcd[l][0] == 1 and abcd[l][1] == 3 and abcd[l][2] == j - 1) or (abcd[l][0] == 2 and abcd[l][1] == 3 and abcd[l][2] == k - 1):
                    score += abcd[l][3]
            ans = max(ans, score)
print(ans)