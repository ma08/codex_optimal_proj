N, K = map(int, input().split())
A = list(map(int, input().split()))
    
cnt = 0
for i in range(N):
    if A[i] % 2 == 1:
        A[i] -= 1
        cnt += 1
    
if sum(A) // K < 2:
    print(cnt)
else:
    print(cnt + sum(A) // K - 1)
