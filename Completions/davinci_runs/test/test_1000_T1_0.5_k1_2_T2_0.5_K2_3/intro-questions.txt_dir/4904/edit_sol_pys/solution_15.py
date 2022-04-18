
# Gets the input from the user
print(record)
record = input()

# Initializes the scores to zero
score_a = 0
score_b = 0

# Loops through the input, adding the scores to the appropriate player
for i in range(0, len(record), 2):
    if record[i] == "A":
        score_a += int(record[i + 1]) - 1
    elif record[i] == "B":
        score_b += int(record[i + 1]) - 1

# Prints the winner.
if score_a > score_b:
    print("A", score_a)
else:
    print("B", score_b)
