

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
a = list(map(int, input().split()))

left = []
right = []

# get the left and right k-th elements

for i in range(1, n):
    left.append(max(left[i-1], a[i-1]))
    right.append(max(right[n-i-1], a[n-i-1]))

ans = []
for i in range(n):
    if left[i] == max(left[i], right[i-1]):
        ans.append(1)
    else:
        ans.append(2)

print("".join(map(str, ans)))
