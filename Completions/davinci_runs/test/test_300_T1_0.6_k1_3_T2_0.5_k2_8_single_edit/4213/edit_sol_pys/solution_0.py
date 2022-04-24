N = int(input())
A = list(map(int, input().split()))

max_diff = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        max_diff = max(max_diff, abs(A[i] - A[j]))

print(max_diff)
