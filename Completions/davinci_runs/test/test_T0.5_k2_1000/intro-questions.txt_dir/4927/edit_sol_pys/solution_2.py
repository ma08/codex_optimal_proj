
import sys

# Grab the input
N, P, Q = map(int, sys.stdin.readline().split())

# Calculate the number of rounds played
rounds_played = P + Q

# Calculate the number of rounds per player
rounds_per_player = 2 * N

# Calculate the number of rounds before the first player serves
rounds_before_first_player_serve = N

# Calculate the number of rounds before the second player serves
rounds_before_second_player_serve = 2 * N

# Calculate the number of rounds before the first player serves again
rounds_before_first_player_serves_again = 3 * N

# Calculate the number of rounds before the second player serves again
rounds_before_second_player_serves_again = 4 * N

# Calculate the number of complete rounds
complete_rounds = rounds_played // rounds_per_player

# Calculate the number of rounds played in the current round
rounds_played_current_round = rounds_played - (complete_rounds * rounds_per_player)

if rounds_played_current_round == 0:
    print("paul")
elif rounds_played_current_round < rounds_before_first_player_serves_again:
    print("paul")
else:
    print("opponent")
