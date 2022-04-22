

N = int(input())
h = list(map(int,input().split()))

cnt = 1
for i in range(1,N):
    if h[i] < h[i-1]:
        cnt += 1
print(cnt-1)
