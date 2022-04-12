
# Use a greedy algorithm
# For each minion, find the highest temperature that is available in a room
# If none is available, create a new room with that temperature

n = int(input())
minions = []
rooms = []

for i in range(n):
    l, u = map(int, input().split())
    minions.append((l, u))

for i in range(n):
    m = minions[i]
    available = True
    for r in rooms:
        if m[0] <= r:
            available = False
            break
    if available:
        rooms.append(m[1])

print(len(rooms))
