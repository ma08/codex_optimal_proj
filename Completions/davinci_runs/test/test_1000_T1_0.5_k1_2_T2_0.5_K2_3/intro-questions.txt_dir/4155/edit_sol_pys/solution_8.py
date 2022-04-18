

N, K = list(map(int,input().split()))
h = list(map(int,input().split()))[:N]
h.sort()
ans = 10**10
for i in range(N-K+1):
    ans = min(ans,h[i+K-1]-h[i])
print(ans)



