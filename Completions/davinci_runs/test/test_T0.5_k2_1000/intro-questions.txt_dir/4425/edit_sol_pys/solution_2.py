
import sys
import math

N, K = map(int, input().split())

# N-sided dice
probability_dice = 1/N

# Coin
probability_coin = 1/2

# Probability that Snuke wins
probability_win = 0

for i in range(1, N+1):
    # Number of times Snuke needs to flip the coin to reach K
    num_flips = math.ceil(math.log2(K/i))

    # Probability that Snuke wins with the current dice
    probability_win_dice = probability_coin**num_flips

    # Probability that Snuke wins
    probability_win += probability_win_dice * probability_dice

print(probability_win)
