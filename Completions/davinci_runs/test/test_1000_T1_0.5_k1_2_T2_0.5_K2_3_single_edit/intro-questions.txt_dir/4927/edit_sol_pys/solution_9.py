

import sys

# Grab the input
N, P, Q = map(int, sys.stdin.readline().split())

# Calculate the number of rounds played
rounds_played = P + Q

if rounds_played % 2 == 0:
    print("paul")
else:
    print("opponent") 
