

# Solution

import math

n, k = map(int, input().split())
a = list(map(int, input().split()))


def count(arr, x):
    return arr.count(x)


def min_ops(arr, k):
    min_num = min(arr)
    min_count = count(arr, min_num)
    if min_count >= k:
        return 0
    else:
        return math.ceil(math.log(k / min_count, 2))


print(min_ops(a, k))