

from sys import stdin

n, p, m = map(int, stdin.readline().split())

players = {}
for i in range(n):
    players[stdin.readline().strip()] = 0

for i in range(m):
    name, score = map(str, stdin.readline().split())
    players[name] += int(score)

winners = [name for name in players.keys() if players[name] >= p]

if len(winners) == 0:
    print("No winner!")
else:
    for winner in winners:
        print(winner + " wins!")
