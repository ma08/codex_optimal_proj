
import sys
import math

N, K = map(int, input().split())

# N-sided die
probability_die = 1 / N

# Coin
probability_coin = 1 / 2

# Probability that Snuke wins
probability_win = 0

for i in range(1, N + 1):
    # Number of times Snuke needs to flip the coin to reach K
    num_flips = math.ceil(math.log2(K/i))

    # Probability that Snuke wins with the current die
    probability_win_die = probability_coin**num_flips

    # Probability that Snuke wins
    probability_win += probability_win_die * probability_die

print(probability_win)
