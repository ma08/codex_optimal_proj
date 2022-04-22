

N, X = map(int, input().split())  # 入力
L = list(map(int, input().split()))  # 入力

cnt = 1  # 個数
dist = 0  # 距離
for i in range(N):
    dist += L[i]
    if dist <= X:
        cnt += 1
    else:
        break
print(cnt)
