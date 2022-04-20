

# SOLUTION
# Input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Preprocessing
for i in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    a[l] -= 1
    if r < n - 1:
        a[r + 1] += 1

# Calculate
for i in range(1, n):
    a[i] += a[i - 1]

# Output
print(max(a) - min(a))
print(0)