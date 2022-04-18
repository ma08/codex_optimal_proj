

N = int(input())
h = list(map(int,input().split()))

cnt = 1
for i in range(1, N):
    if h[i-1] >= h[i]:
        cnt += 1
print(N - cnt)
