

# SOLUTION
# This is a math problem.
# If we have an array of length n, and the sum is m, then the max diff is m - n.
# If we have an array of length n, and the sum is less than m, then the max diff is sum - n.
# If we have an array of length n, and the sum is greater than m, then the max diff is m - n.

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(max(m - n, 0))