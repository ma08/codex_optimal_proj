

from sys import stdin

n, p, m = [int(x) for x in stdin.readline().split()]  # number of players, points needed to win, number of rounds

players = {}
for i in range(n):
    players[stdin.readline().rstrip()] = 0  # add player to dictionary with score 0

for i in range(m):
    name, score = stdin.readline().split()
    players[name] += int(score)  # add score to player

winners = [name for name in players.keys() if players[name] >= p]  # check if there are any players with score >= p

if len(winners) == 0:
    print("No winner!")
else:
    for winner in winners:
        print(winner + " wins!")
