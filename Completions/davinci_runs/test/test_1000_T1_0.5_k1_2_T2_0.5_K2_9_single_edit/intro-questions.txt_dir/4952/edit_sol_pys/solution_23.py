import sys

numVotes = 0
votes = []

for line in sys.stdin:
    line = line.strip()
    if line == '***':  # end of input
        break
    numVotes += 1  # count number of votes
    votes.append(line)

candidates = {}  # dictionary of candidates
for vote in votes:  # count votes for each candidate
    if vote in candidates:
        candidates[vote] += 1
    else:
        candidates[vote] = 1

maxVotes = 0  # highest number of votes
winner = ''  # candidate with highest number of votes
for candidate, numVotes in candidates.items():  # find highest number of votes
    if numVotes > maxVotes:
        maxVotes = numVotes
        winner = candidate

if maxVotes > numVotes / 2:  # highest number of votes is majority
    print(winner)
else:  # highest number of votes is not majority
    print('Runoff!')
