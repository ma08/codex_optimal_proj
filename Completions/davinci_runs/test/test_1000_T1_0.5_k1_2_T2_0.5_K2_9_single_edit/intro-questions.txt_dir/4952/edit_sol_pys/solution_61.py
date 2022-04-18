import sys

numVotes = 0
votes = []

for line in sys.stdin:
    line = line.strip()
    if line == '***':
        break
    numVotes += 1
    votes.append(line)

candidates = {}
for vote in votes:
    if vote in candidates:
        candidates[vote] += 1
    else:
        candidates[vote] = 1

maxVotes = 0
winner = ''
for candidate, votes in candidates.items():
    if votes > maxVotes:
        maxVotes = votes
        winner = candidate

if maxVotes > numVotes/2:
    print(winner)
else:
    print('Runoff!')
