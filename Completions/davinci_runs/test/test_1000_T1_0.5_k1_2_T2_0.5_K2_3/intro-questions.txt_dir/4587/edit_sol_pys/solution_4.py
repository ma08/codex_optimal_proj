N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N): 
    if i == 0: 
        ans = A[i]
        continue
    if A[i] > K:
        ans += K
    else:
        ans += A[i]
print(ans) 
