

# Problem

"""
Given an array of integers, remove the smallest value. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
"""

# Solution 

n = int(input())
a = list(map(int, input().split()))

s = set()
for i in range(n):
    if a[i] not in s:
        s.add(a[i])
    else:
        s.remove(a[i])

print(n-len(s))
