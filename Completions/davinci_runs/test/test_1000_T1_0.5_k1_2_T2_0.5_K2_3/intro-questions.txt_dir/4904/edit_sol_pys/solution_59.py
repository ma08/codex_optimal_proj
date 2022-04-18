
record = input() # Gets the input from the user

score_a = 0 # Initializes the scores to zero
score_b = 0 # Initializes the scores to zero

for i in range(len(record)): # Loops through the input, adding the scores to the appropriate player
    if record[i] == "A":
        score_a += int(record[i + 1])
    elif record[i] == "B":
        score_b += int(record[i + 1])

if score_a > score_b: # Prints the winner
    print("A")
else:
    print("B")
