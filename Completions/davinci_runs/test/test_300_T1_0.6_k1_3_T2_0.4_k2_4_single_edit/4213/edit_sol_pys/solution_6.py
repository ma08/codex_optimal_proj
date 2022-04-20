N = int(input())
A = [int(i) for i in input().split()]  # list comprehension

max_diff = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        max_diff = max(max_diff, abs(A[i] - A[j]))  # max(a, b)

print(max_diff)
