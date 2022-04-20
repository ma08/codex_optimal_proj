

# SOLUTION
# The problem is solved by binary search.
# The idea is to find the smallest number x such that k elements of the array are less than or equal to x
# This can be done by binary search on the array.
# The time complexity is O(n log n)

from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))

a.sort()

lo = 1
hi = 10**9

while lo <= hi:
    mid = (lo + hi) // 2
    count = 0
    for i in range(n):
        if a[i] <= mid:
            count += 1
        else:
            break
    if count == k:
        stdout.write(str(mid))
        exit()
    elif count < k:
        lo = mid + 1
    else:
        hi = mid - 1

stdout.write('-1')
