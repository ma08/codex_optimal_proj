
# Initializes the scores to zero
score_a = 0
score_b = 0

# Reads the input
with open("input.txt", "r") as f:
    # Loops through the input, adding the scores to the appropriate player
    for line in f:
        for i in range(len(line)):
            if line[i] == "A":
                score_a += int(line[i + 1])
            elif line[i] == "B":
                score_b += int(line[i + 1])

# Prints the winner
if score_a > score_b:
    print("A")
else:
    print("B")
