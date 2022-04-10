

# Read input
N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

# Initialize players' scores
scores = [K] * N

# Update players' scores
for i in range(Q):
    for j in range(N):
        if j == A[i] - 1:
            continue
        else:
            scores[j] -= 1

# Output
for i in range(N):
    if scores[i] <= 0:
        print('No')
    else:
        print('Yes')