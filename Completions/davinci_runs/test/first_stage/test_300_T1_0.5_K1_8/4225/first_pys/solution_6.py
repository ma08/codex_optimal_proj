

# The maximum possible sum is obtained by picking up all cards with 1s,
# and then picking up as many cards with 0s as possible.
# The number of cards with 0s that can be picked up is K - A.

A, B, C, K = map(int, input().split())
print(A + min(B, K - A))