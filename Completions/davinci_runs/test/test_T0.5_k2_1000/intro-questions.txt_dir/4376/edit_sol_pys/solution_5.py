import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dorm_sum = [0] * (n+1)
for i in range(1, n+1):
    dorm_sum[i] = dorm_sum[i-1] + a[i-1]

for query in b: print(binary_search(dorm_sum, query))

def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid
    return left
