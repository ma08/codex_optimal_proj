

# SOLUTION
# This problem is quite easy.
# The maximum possible sum of absolute differences between adjacent elements
# is obtained when the array is sorted (or reversed sorted).
# The answer is then the sum of all differences between consecutive elements.
# The differences are the same as the element itself,
# so the answer is the sum of all elements of the array.
# As the array must have a sum of m,
# the answer is m*(n-1).

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(m*(n-1))