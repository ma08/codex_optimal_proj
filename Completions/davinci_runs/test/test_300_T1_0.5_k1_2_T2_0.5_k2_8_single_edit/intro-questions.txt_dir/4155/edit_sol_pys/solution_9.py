
N = int(input())
h = list(map(int,input().split()))

cnt = h[0]
for i in range(N):
    if h[i] > cnt:
        cnt = h[i]
print(cnt)
