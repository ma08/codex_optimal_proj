
# Get the input from the user
record = input()

# Initialize the scores to zero
score_a = 0
score_b = 0

# Loop through the input, adding the scores to the appropriate player
for i in range(len(record)):
    if record[i] == "A":
        score_a += int(record[i + 1])
    elif record[i] == "B":
        score_b += int(record[i + 1])

# Prints the winner
if score_a > score_b:
    print('A')
else:
    print('B')
