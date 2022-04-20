

N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] + K <= 5:
        A[i] = 0
    else:
        A[i] = 1
print(A.count(0) // 3)
