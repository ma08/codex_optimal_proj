
import sys
import math

N, K = map(int, sys.stdin.readline().split())

# Probability that Snuke wins
probability_win = 0

# Probability that Snuke loses
probability_lose = 0

# Coin
probability_coin = 1/2

# N-sided die
probability_die = 1/N

for i in range(1, N+1):
    # Number of times Snuke needs to flip the coin to reach K
    num_flips = math.ceil(math.log2(K/i))

    # Probability that Snuke wins with the current die
    probability_win_die = probability_coin**num_flips * probability_die

    # Probability that Snuke loses with the current die
    probability_lose_die = (1 - probability_coin**num_flips) * probability_die

    # Probability that Snuke wins
    probability_win += probability_win_die
    probability_lose += probability_lose_die

print(probability_lose)
    probability_win += probability_win_die * probability_die

print(probability_win)
