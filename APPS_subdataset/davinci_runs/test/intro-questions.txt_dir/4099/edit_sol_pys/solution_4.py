
# Read inputs
n, k, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

# Add up the scores from the previous subjects
total = 0
for i in range(n - 1):
    total += a[i]

# If the goal is impossible, print -1
if total / (n - 1) < m:
    print(-1)
# Otherwise, print the minimum number of points required
else:
    # The minimum number of points required is the maximum of the goal score and the minimum possible score
    print(max(m * n - total, 0))
