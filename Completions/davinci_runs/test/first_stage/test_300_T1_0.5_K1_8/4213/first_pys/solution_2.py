

N = int(input())
A = list(map(int, input().split()))

max_diff = 0
for i in range(N):
    for j in range(N):
        if i != j:
            diff = abs(A[i] - A[j])
            if diff > max_diff:
                max_diff = diff

print(max_diff)