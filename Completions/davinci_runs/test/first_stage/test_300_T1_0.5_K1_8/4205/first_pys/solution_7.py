

N = int(input())
p = list(map(int, input().split()))

# 初期化
ans = 'NO'
for i in range(N):
    if p[i] == i + 1:
        continue
    else:
        # 入れ替えられる数字の判定
        if i + 1 in p:
            # 入れ替えられる数字のインデックスを取得
            j = p.index(i + 1)
            p[i], p[j] = p[j], p[i]
            ans = 'YES'
            break

print(ans)