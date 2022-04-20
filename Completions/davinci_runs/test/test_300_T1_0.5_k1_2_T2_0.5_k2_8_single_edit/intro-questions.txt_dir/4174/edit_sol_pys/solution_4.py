
N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 1
distance = 0
for i in range(N):
    distance += L[i]
    if distance <= X:
        cnt += 1
    else:
        break
print(cnt)
