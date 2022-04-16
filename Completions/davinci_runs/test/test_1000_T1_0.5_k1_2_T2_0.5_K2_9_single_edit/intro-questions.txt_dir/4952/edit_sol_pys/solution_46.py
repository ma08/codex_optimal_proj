import sys
from collections import defaultdict
from collections import Counter


votes = defaultdict(int)

for line in sys.stdin:
    vote = line.strip()
    if vote == '***':
        break
    else:
        votes[vote] += 1

counts = Counter(votes.values())

if len(counts) == 1:
    print(list(votes.keys())[0])
else:
    max_votes = max(counts.keys())
    winners = [k for k, v in votes.items() if v == max_votes]
    if len(winners) == 1:
        print(winners[0])
    else:
        print('Runoff!')
