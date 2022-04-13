import sys
lines = sys.stdin.readlines()
R, S = [int(x) for x in lines[0].split()]
seating = [list(s.strip()) for s in lines[1:]]


def handshakes(seating):
    count = 0
    for row in range(R):
        for seat in range(S):
            if seating[row][seat] == "o":
                # Check left
                if seat > 0 and seating[row][seat - 1] == "o":
                    count += 1
                # Check right
                if seat < S - 1 and seating[row][seat + 1] == "o":
                    count += 1
                # Check up
                if row > 0 and seating[row - 1][seat] == "o":
                    count += 1
                # Check down
                if row < R - 1 and seating[row + 1][seat] == "o":
                    count += 1
                # Check up left
                if seat > 0 and row > 0 and seating[row - 1][seat - 1] == "o":
                    count += 1
                # Check up right
                if seat < S - 1 and row > 0 and seating[row - 1][seat + 1] == "o":
                    count += 1
                # Check down left
                if seat > 0 and row < R - 1 and seating[row + 1][seat - 1] == "o":
                    count += 1
                # Check down right
                if seat < S - 1 and row < R - 1 and seating[row + 1][seat + 1] == "o":
                    count += 1
    return count

print(handshakes(seating))
