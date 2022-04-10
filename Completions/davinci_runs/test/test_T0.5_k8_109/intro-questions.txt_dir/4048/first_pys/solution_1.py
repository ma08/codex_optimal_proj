

# Read input
N = int(input())

# Initialize
moves = 0

# Loop until N is reached
while N > 1:
    # If N is even, divide by 2
    if N % 2 == 0:
        N //= 2
    # If N is odd, subtract 1
    else:
        N -= 1
    # Increase number of moves
    moves += 1

# Print result
print(moves)