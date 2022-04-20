

N = int(input())
A = list(map(int, input().split()))

max_value = A[0]
min_value = A[0]

for i in range(1, N):
    max_value = max(max_value, A[i])
    min_value = min(min_value, A[i])

print(max_value - min_value)