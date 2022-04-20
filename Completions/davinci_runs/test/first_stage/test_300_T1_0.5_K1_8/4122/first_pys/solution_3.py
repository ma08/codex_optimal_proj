

# First attempt
# Read input
h, n = map(int, input().split())
d = [int(i) for i in input().split()]

# Initialize the monster's current health
curr_h = h

# Iterate through the list of damage values
for i in range(n):
    # Calculate the new health
    curr_h += d[i]
    # If the monster's health is <= 0, print the current round and break
    if curr_h <= 0:
        print(i + 1)
        break
# Else, print -1 (no round will kill the monster)
else:
    print(-1)

# Second attempt
# Read input
h, n = map(int, input().split())
d = [int(i) for i in input().split()]

# Initialize the monster's current health
curr_h = h

# Iterate through the list of damage values
for i in range(n):
    # Calculate the new health
    curr_h += d[i]
    # If the monster's health is <= 0, print the current round and break
    if curr_h <= 0:
        print(i + 1)
        break
# Else, print -1 (no round will kill the monster)
else:
    print(-1)