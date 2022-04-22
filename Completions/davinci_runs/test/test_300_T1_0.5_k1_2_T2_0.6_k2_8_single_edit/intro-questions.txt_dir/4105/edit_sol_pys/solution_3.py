
import math

n, k, m = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]


def bs(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


def is_possible(num):
    for i in range(n):
        if bs(a, num - a[i]) > i and bs(a, num - a[i]) != -1:
            return True
    return False


ans = 0
for i in range(k):
    if is_possible(m - i):
        ans = m - i
        break

print(ans)
