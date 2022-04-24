
N, X = map(int, input().split()) #N:個数 X:距離
L = list(map(int, input().split())) #L:距離の配列

cnt = 1 #個数
dist = 0 #距離
for i in range(N):
    dist += L[i]
    if dist <= X:
        cnt += 1
    else:
        break
print(cnt)
