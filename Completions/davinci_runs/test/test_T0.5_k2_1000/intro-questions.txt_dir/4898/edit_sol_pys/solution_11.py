

# Use a greedy algorithm
# For each minion, find the lowest temperature that is available in the rooms
# If none is available, create a new room with that temperature and put the minion in it
n = int(input())
minions = [0] * n
rooms = [0] * n

for i in range(n):
    l, u = map(int, input().split())
    minions[i] = (l, u)

for i in range(n):
    m = minions[i]
    available = False
    for r in rooms:
        if m[0] <= r <= m[1]:
            available = True
            break
    if not available:
        rooms[i] = m[0]

print(len(rooms))
