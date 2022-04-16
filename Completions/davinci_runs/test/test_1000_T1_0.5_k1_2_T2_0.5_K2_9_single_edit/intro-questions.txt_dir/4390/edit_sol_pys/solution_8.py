
# SOLUTION
# This is just a simple application of modulo operation.
# The minimum number of moves will be the difference between
# a and the remainder when a is divided by b.
# Runtime: O(1)

t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    print(A % B)
