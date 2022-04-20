

n, k = map(int, input().split())
a = list(map(int, input().split()))

# First, find the maximum value in the array.
max_a = max(a)

# Then, find the minimum number of operations needed to get all of the elements to be equal to the maximum value.
# This is the same as finding the minimum number of operations needed to get all of the elements to be equal to 1,
# since the maximum value is a power of 2.
count = 0
for i in range(n):
    count += a[i] - 1

# If the number of operations needed to get all of the elements to be equal to 1 is less than or equal to k,
# then the minimum number of operations needed is simply the number of operations needed to get all of the elements
# to be equal to 1.
if count <= k:
    print(count)

# If the number of operations needed to get all of the elements to be equal to 1 is greater than k, then the minimum
# number of operations needed is k, since that is the maximum number of operations that can be done.
else:
    print(k)