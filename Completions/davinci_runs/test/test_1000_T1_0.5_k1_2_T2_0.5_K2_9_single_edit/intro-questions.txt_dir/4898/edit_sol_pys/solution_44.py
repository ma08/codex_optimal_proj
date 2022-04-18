

# Use a greedy algorithm
# For each minion, find the lowest temperature that is available
# If none is available, create a new room with that temperature
from collections import deque
n = int(input())
minions = deque()
rooms = []

for i in range(n):
    l, u = map(int, input().split())
    minions.append([l, u])

for i in range(n):
    m = minions.popleft()
    available = False
    for r in rooms:
        if m[0] <= r <= m[1]:
            available = True
            break
    if not available:
        rooms.append(m[0])

print(len(rooms))
