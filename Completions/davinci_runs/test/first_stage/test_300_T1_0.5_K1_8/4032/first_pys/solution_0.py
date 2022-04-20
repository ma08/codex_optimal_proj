

n, k = map(int, input().split())
diffs = list(map(int, input().split()))

left, right = 0, n-1

while left <= right and diffs[left] <= k:
    left += 1
while left <= right and diffs[right] <= k:
    right -= 1

print(left + n - 1 - right)