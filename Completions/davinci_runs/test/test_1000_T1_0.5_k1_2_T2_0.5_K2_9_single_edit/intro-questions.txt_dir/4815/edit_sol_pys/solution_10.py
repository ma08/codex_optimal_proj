'''
You are given a list of players and their scores. Print the name of the player with the highest score. If there are multiple players with the same score, print all of their names.
'''
# read the inputs
import sys

n, p, m = [int(x) for x in sys.stdin.readline().split()]
players = []
for i in range(n):
    players.append(sys.stdin.readline().strip())
# create a dictionary with the players as keys and their scores as values
scores = {x: 0 for x in players}
# update the scores
for i in range(m):
    line = sys.stdin.readline().strip().split()
    scores[line[0]] += int(line[1])
# find the winners
winners = []
for player in players:
    if scores[player] >= p:
        winners.append(player)
# print the winners
if len(winners) > 0:
    for winner in winners:
        print(winner + " wins!")
else:
    print("No winner!")
