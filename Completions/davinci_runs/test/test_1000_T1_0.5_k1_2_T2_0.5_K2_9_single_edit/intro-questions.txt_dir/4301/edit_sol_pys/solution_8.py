

N = int(input())
A = list(map(int, input().split()))
max_a = max(A) - 1
for i in range(N):
    print(max_a if A[i] != max(A) else max(A))
