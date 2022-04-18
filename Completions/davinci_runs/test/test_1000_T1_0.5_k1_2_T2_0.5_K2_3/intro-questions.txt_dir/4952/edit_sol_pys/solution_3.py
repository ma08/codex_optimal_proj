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
    print(list(votes.keys())[0]) #print the first key in dictionary
else:
    max_votes = max(votes.values()) #find the max value in dictionary
    winners = [k for k, v in votes.items() if v == max_votes] #find the key for the max value
    if len(winners) == 1:
        print(winners[0])
    else:
        print('Runoff!')
