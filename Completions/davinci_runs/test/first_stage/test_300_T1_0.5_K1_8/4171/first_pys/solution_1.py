

# Solution
import math

n, k = map(int, input().split())
a = [int(x) for x in input().split()]

# Find the maximum element in the array
max_val = max(a)

# Find the maximum number of operations required to make all elements equal
# We can do this by finding the number of bits in the maximum element
max_op = math.floor(math.log(max_val, 2))

# Find the minimum number of operations required to make all elements equal
# We can do this by finding the number of bits in the minimum element
min_op = math.floor(math.log(min(a), 2))

# If the number of operations required to make all elements equal is less than the number of operations required to make at least k elements equal, print the former
if n * min_op <= k * max_op:
    print(min_op)
# Otherwise, print the latter
else:
    print(max_op)