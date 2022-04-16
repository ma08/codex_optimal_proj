
import os
import sys
from sys import stdin


if os.name == 'posix' and sys.version_info[0] < 3:
    import subprocess
    p = subprocess.Popen(['stty', '-icanon'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    p.communicate()
n, p, m = [int(x) for x in stdin.readline().split()]

players = {}
for i in range(n):
    players[stdin.readline().rstrip()] = 0

for i in range(m):
    name, score = stdin.readline().split()
    players[name] += int(score)

winners = [name for name in players.keys() if players[name] >= p]

if len(winners) == 0:
    print("No winner!")
else:
    for winner in winners:
        print(winner + " wins!")
