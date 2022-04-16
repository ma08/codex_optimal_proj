

import sys
import math

N, K = map(int, input().split())

# Probability that Snuke wins a game
probability_win_game = 1/N

# Probability that Snuke wins
probability_win = 0

# Number of times Snuke needs to flip the coin to reach K
num_flips = math.ceil(math.log2(K/probability_win_game))
probability_win = probability_win_game * (1/2)**num_flips

print(probability_win)
