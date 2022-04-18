

import sys

lines = sys.stdin.readlines()

R, S = [int(x) for x in lines[0].split()]

seating = [list(s.strip()) for s in lines[1:]]

def handshakes(seating):
    count = 0
    for i in range(R):
        for j in range(S):
            if seating[i][j] == "o":
                if j > 0 and seating[i][j - 1] == "o":
                    count += 1 # Check left
                if j < S - 1 and seating[i][j + 1] == "o":
                    count += 1 # Check right
                if i > 0 and seating[i - 1][j] == "o":
                    count += 1 # Check up
                if i < R - 1 and seating[i + 1][j] == "o":
                    count += 1 # Check down
                if j > 0 and i > 0 and seating[i - 1][j - 1] == "o":
                    count += 1 # Check up-left
                if j < S - 1 and i > 0 and seating[i - 1][j + 1] == "o":
                    count += 1 # Check up-right
                if j > 0 and i < R - 1 and seating[i + 1][j - 1] == "o":
                    count += 1 # Check down-left
                if j < S - 1 and i < R - 1 and seating[i + 1][j + 1] == "o":
                    count += 1 # Check down-right
    return count

print(handshakes(seating))
