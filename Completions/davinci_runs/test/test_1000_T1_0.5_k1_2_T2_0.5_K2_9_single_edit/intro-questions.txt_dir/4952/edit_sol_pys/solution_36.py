import sys

num_votes = 0
votes = []

for line in sys.stdin:
    line = line.strip()
    if line == '***':
        break
    num_votes += 1
    votes.append(line)

candidates = {}
for vote in votes:
    if vote in candidates:
        candidates[vote] += 1
    else:
        candidates[vote] = 1

max_votes = 0
winner = ''
for candidate, num_votes in candidates.items():
    if num_votes > max_votes:
        max_votes = num_votes
        winner = candidate

if max_votes > num_votes/2:
    print(winner)
else:
    print('Runoff!')
