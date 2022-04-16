

# Use a greedy algorithm. For each minion, find the lowest temperature that is available. If none is available, create a new room with that temperature.

n = int(input()) # number of minions
minions = []
rooms = []

    # tuple of lower and upper temperature bounds for each minion
for i in range(n):
    l, u = map(int, input().split())
    minions.append((l, u))
# for each minion, check if there is a room that meets the temperature requirements

for i in range(n):
    # set default to false
    m = minions[i]
    available = False
        # if temperature is between the bounds, the minion is satisfied
    for r in rooms:
        if m[0] <= r <= m[1]:
            available = True
            break
    if not available:
        # if no room meets the requirements, create a new room with the lower bound temperature
        rooms.append(m[0])

print(len(rooms))
