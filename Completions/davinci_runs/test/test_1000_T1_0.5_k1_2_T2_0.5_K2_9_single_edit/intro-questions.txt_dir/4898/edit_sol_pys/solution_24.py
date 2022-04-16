

# Use a greedy algorithm. For each minion, find the lowest temperature that is available. If none is available, create a new room with that temperature

n = int(input())
minions = [] # List of tuples containing the lower and upper bounds of the minion
rooms = [] # List of temperatures that have been assigned to rooms

    # Read in the lower and upper bounds of the minion
for i in range(n):
    l, u = map(int, input().split())
    minions.append((l, u)) # Add the minion to the list

    # Get the minion
for i in range(n):
    # Check if there is a room with a temperature within the minion's bounds
    m = minions[i]
    available = False
    for r in rooms:
        if m[0] <= r <= m[1]:
            available = True
            break
    if not available:
        # If no room is available, create a new room with the lower bound of the minion
        rooms.append(m[0])

# Print the number of rooms created
print(len(rooms))
