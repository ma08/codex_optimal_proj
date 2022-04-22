

def find_min_arr(n, k, arr):
    arr.sort()

n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

l = 1
r = max(arr)
while l < r:
    m = (l + r) // 2
    if sum([x // m for x in arr]) >= k:
        l = m + 1
    else:
        r = m
print(l)
