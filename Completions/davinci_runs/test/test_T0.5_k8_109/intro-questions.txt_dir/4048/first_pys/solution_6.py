

import math

N = int(input())

# The minimum number of moves needed to reach a square that contains N is
# the sum of the minimum number of moves needed to reach a square that contains
# the largest square number that is smaller than N and the number of moves needed
# to reach the square that contains N from the square that contains the largest
# square number that is smaller than N.
# Because Takahashi can only move right and down, it is enough to calculate the
# minimum number of moves needed to reach a square that contains the largest
# square number that is smaller than N.

# Find the largest square number that is smaller than N.
largest_sq = int(math.floor(math.sqrt(N)))

# Find the minimum number of moves needed to reach a square that contains the
# largest square number that is smaller than N.
# The minimum number of moves needed to reach a square that contains n is n - 1
# because Takahashi can reach a square that contains n from a square that contains 1
# in n - 1 moves.
print(largest_sq - 1 + N - largest_sq ** 2)