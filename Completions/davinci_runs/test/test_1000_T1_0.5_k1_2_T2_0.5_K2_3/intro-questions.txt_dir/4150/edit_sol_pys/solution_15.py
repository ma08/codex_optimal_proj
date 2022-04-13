
# SOLUTION
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

left = [0] * n
right = [0] * n

# get the left and right k-th max element
for i in range(1, n):
    left[i] = max(left[i-1], a[i-1])
    right[n-i-1] = max(right[n-i], a[n-i])

ans = [0] * n
for i in range(n):
    if left[i] == max(left[i], right[i]):
        ans[i] = 1
    else:
        ans[i] = 2

print("".join(map(str, ans)))
