
N, D = map(int, input().split())

# The minimum number of inspectors is the maximum number of trees that can be
# inspected by one inspector. This can be achieved by placing an inspector at
# the leftmost tree that can inspect the rightmost tree.
print(-(-N // (2 * D + 1)))
