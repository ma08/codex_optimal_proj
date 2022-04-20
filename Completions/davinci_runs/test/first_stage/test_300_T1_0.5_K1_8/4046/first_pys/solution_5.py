

n = int(input())
q = list(map(int, input().split()))

# Check if the sequence is possible
for i in range(n-1):
    if abs(q[i]) > 1:
        print(-1)
        exit()

# Create the sequence
p = [0]*n
p[0] = q[0]
for i in range(1,n):
    p[i] = p[i-1] + q[i-1]

# Check if the sequence is a permutation
if len(set(p)) != n or min(p) < 1 or max(p) > n:
    print(-1)
    exit()

# Print the sequence
for i in range(n):
    print(p[i], end=' ')