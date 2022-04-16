

import sys

# Grab the input
N, P, Q = map(int, sys.stdin.readline().split())

# Calculate the number of rounds played
rounds_played = P + Q

# Calculate the number of rounds per player
rounds_per_player = 2 * N

# Calculate the number of complete rounds
complete_rounds = rounds_played // rounds_per_player

# Calculate the number of rounds played in the current round
rounds_played_current_round = rounds_played - (complete_rounds * rounds_per_player)

if rounds_played_current_round == 0:
    print("paul")
elif rounds_played_current_round < 3 * N:
    print("paul")
else:
    print("opponent")
