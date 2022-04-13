import sys

num_votes = 0
votes = []

for line in sys.stdin:
    line = line.strip()
    if line == '***':
        break
    num_votes += 1
    votes.append(line)

if num_votes > 0:
    candidate_dict = {}
    for vote in votes:
        if vote in candidate_dict:
            candidate_dict[vote] += 1
        else:
            candidate_dict[vote] = 1

    max_votes = 0
    winner = ''
    for candidate, num_votes in candidate_dict.items():
        if num_votes > max_votes:
            max_votes = num_votes
            winner = candidate

    if max_votes > num_votes/2:
        print(winner)
    else:
        print('Runoff!')
