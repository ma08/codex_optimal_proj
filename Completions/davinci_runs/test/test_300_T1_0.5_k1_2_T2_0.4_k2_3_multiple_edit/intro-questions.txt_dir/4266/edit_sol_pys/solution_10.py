import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

left = 0
right = n

while left < right:
    mid = (left + right) // 2
    if a[mid] == m:
        print(mid + 1)
        sys.exit()
    elif a[mid] < m:
        left = mid + 1
    else:
        right = mid

print(0)
