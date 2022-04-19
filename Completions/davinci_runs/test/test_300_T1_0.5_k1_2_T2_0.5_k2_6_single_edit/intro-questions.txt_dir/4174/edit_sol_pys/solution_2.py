
N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 1
dist = 0
for i in range(N-1):
    dist += L[i]
    if dist <= X:
        cnt += 1
    else:
        break
print(cnt)
