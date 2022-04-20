

import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# The minimum number of operations is the minimum number of operations required to make all elements equal to the minimum element.
# Since we can divide all elements by two, we need to find the largest power of two in the array.
# We can do this by finding the maximum number of trailing zeros in the binary representation of all elements.

max_zeros = 0
for i in a:
    cur_zeros = 0
    while i % 2 == 0:
        i //= 2
        cur_zeros += 1
    max_zeros = max(max_zeros, cur_zeros)

print(max_zeros)