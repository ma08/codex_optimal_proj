
# SOLUTION
# This is just a simple application of modulo operation.
# The minimum number of moves will be the remainder when
# a and the remainder when a is divided by b.
# Runtime: O(t)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a % b)
