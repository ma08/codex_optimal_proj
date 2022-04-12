N, X = map(int, input().split())
L = list(map(int, input().split())) # 入力をリスト化

cnt = 1
dist = 0
for i in range(N):
    dist += L[i] # 距離を足していく
    if dist <= X:
        cnt += 1 # 距離がX以下ならカウントを増やす
    else:
        break
print(cnt)
