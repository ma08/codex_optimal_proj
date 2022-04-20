

N = int(input())
h = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if h[i] == 0:
        continue
    for j in range(i, N):
        if h[j] == 0:
            continue
        if h[j] == h[i]:
            cnt += 1
            for k in range(i, j+1):
                h[k] -= 1
            break
        elif h[j] < h[i]:
            cnt += 1
            for k in range(i, j+1):
                h[k] -= 1
            break

print(cnt)