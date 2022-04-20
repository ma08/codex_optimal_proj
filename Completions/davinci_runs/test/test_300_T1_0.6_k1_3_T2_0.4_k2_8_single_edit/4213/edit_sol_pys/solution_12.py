N = int(input())
A = [int(n) for n in input().split()]

max_diff = 0
for i in range(N):
    for j in range(N):
        if i != j:
            max_diff = max(max_diff, abs(A[i] - A[j]))

print(max_diff)
