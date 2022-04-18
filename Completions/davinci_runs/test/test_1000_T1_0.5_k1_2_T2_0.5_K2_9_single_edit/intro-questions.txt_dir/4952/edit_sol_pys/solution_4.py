
import sys

votes = {}

for line in sys.stdin:
    vote = line.strip()
    if vote == '***':
        break
    else:
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1

total = sum(votes.values())

if len(votes) == 1:
    print(votes.keys()[0])
else:
    max_votes = max(votes.values())
    winners = [k for k, v in votes.items() if v == max_votes]
    if len(winners) == 1:
        print(winners[0])
    else:
        print('Runoff!')
