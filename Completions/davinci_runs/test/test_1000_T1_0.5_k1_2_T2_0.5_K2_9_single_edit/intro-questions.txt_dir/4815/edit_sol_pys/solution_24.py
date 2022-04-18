

from sys import stdin

n, p, m = [int(x) for x in stdin.readline().split()]

players = {}
for i in range(n):
    players[stdin.readline().rstrip()] = 0

for i in range(m):
    name, score = stdin.readline().split()
    players[name] += int(score)

winners = [name for name in players.keys() if players[name] >= p]

if len(winners) == 0:
    print("no winner")
else:
    for winner in winners:
        print(winner + " wins")
