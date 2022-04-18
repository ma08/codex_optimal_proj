
import sys

n, p, m = [int(x) for x in sys.stdin.readline().split()]
players = []
for i in range(n):
    players.append(sys.stdin.readline().strip())  # read players

scores = {x: 0 for x in players}  # dict of scores

for i in range(m):
    line = sys.stdin.readline().strip().split()  # read rounds
    scores[line[0]] += int(line[1])

winners = []
for player in players:  # find winners
    if scores[player] >= p:
        winners.append(player)

if len(winners) > 0:  # output
    for winner in winners:  # winners
        print(winner + " wins!")
else:
    print("No winner!")
