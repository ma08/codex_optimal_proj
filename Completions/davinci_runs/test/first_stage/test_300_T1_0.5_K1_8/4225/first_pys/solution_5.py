

import sys

# Read input
a, b, c, k = [int(i) for i in input().split()]

# Initialize variables
total = a + b + c
nums = [1] * a + [0] * b + [-1] * c

# Sort list
nums.sort()

# If there are enough cards to pick from, we can pick all -1 cards, then all 0 cards, then all 1 cards
if total >= k:
    print(sum(nums[:k]))
# If there are not enough cards to pick from, we can pick all 1 cards, then all 0 cards, then all -1 cards
else:
    print(sum(nums))