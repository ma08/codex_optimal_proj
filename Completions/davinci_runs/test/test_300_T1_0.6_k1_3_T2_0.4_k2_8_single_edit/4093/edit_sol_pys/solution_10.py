

# SOLUTION
# Use pen and paper to visualize the problem
# We want to maximize the sum of absolute differences between adjacent elements
# The sum of the elements of the array is m
# Let's say the max is x. Then we have m - x = x.
# The max can be no more than half the sum of m
# We can build the array by filling in the max,
# then filling in m - max,
# then filling in the max,
# then filling in m - max,
# and so on,
# until we reach the last element.
# We can do this because the sum of the array is m which is an even number

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
    else:
        print(m - 1)
