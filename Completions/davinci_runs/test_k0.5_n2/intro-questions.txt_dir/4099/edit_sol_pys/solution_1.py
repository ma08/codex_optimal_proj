

# Read input
n, k, m = [int(x) for x in input().split()]  # n: number of subjects, k: number of passed subjects, m: goal score
a = [int(x) for x in input().split()]  # a: scores of the passed subjects

# Add up the scores from the passed subjects
total = 0
for i in range(n - 1):
    total += a[i]

# If the goal is impossible, print -1.
if total / (n - 1) < m:
    print(-1)
# Otherwise, print the minimum number of points required
else:
    # The minimum number of points required is the maximum of the goal score and the minimum possible score
    print(max(m * n - total, 0))
