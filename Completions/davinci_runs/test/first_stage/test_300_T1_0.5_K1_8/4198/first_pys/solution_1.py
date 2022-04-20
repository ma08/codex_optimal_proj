

# I think this is a good example of the power of a greedy algorithm.
# It's obvious that we want the largest possible integer for our money,
# but it's not so obvious how to calculate that.
# The greedy approach is to use the fact that the cost of an integer is
# A * N + B * d(N).
# We can see that the cost of an integer is monotonically increasing in N,
# but the cost of an integer is monotonically decreasing in d(N).
# So, we want to use as many digits as possible,
# and we want to use the largest possible digits.
# The largest possible digits are 9, so we want to use 9s as much as possible.
# The cost of the number 9 is 10 * 9 + 7 * 1 = 97,
# so we can buy a 9 for every 97 yen we have.
# Once we've used up all of our 9s, we want to use 8s as much as possible,
# and so on.
# We can also use 0s as much as we want, since they don't cost anything.
# We can use a greedy algorithm to find the largest possible integer for our money.
# We start with the largest digit, 9, and we buy as many 9s as we can.
# Then we move on to the next largest digit, 8, and we buy as many 8s as we can.
# We continue until we run out of money.
# The largest integer we can buy is the concatenation of all the digits we bought.

import sys

# Read in the input.
A, B, X = map(int, sys.stdin.readline().split())

# We start with the largest digit, 9, and we buy as many 9s as we can.
# Then we move on to the next largest digit, 8, and we buy as many 8s as we can.
# We continue until we run out of money.
# The largest integer we can buy is the concatenation of all the digits we bought.
# We can use a greedy algorithm to find the largest possible integer for our money.
# We start with the largest digit, 9, and we buy as many 9s as we can.
# Then we move on to the next largest digit, 8, and we buy as many 8s as we can.
# We continue until we run out of money.
# The largest integer we can buy is the concatenation of all the digits we bought.
answer = ""
for i in range(9, -1, -1):
    # We can buy i if we have enough money to buy at least one of them.
    # The cost of buying one i is A * i + B * 1.
    if X >= A * i + B:
        # We can buy as many i as we have money for.
        # The cost of buying one i is A * i + B * 1,
        # so the cost of buying n i is A * i * n + B * n.
        n = (X - B) // (A * i + B)
        # Add n i to the answer.
        answer += str(i) * n
        # Subtract the cost of buying n i from the money we have.
        X -= (A * i + B) * n

# Print the answer.
print(answer)