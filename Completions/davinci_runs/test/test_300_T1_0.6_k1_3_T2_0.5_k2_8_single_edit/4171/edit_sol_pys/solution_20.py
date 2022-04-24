import sys


n, k = map(int, input().split())
arr = list(map(int, input().split()))

# n, k = 5, 3
# arr = [1, 2, 2, 4, 5]

# n, k = 5, 3
# arr = [1, 2, 3, 4, 5]

# n, k = 5, 3
# arr = [1, 2, 3, 3, 3]

    if min(arr) == 0:
        arr.remove(0)

def run(arr, k):
    count = 0
    while len(set(arr)) > 1:
        count += 1
        arr = list(map(lambda x: x // 2, arr))
        if min(arr) == 0 and len(set(arr)) > 1:
            return -1
    if min(arr) == 0:
        arr.remove(0)
    if len(set(arr)) == 1 and arr.count(arr[0]) >= k:
        return count
    else:
        return -1


print(run(arr, k))
