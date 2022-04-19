N = int(input())
A = list(map(int, input().split()))


B = [0 for i in range(N)]
B[0] = A[0]
B[-1] = A[-1]

for i in range(1, N):
    B[i] = A[i] - B[i-1]
    
print(sum(B))
