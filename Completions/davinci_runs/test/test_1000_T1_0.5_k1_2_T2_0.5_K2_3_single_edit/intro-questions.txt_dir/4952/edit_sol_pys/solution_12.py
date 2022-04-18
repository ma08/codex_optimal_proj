
import sys

def getMajority(votes):
    votes = sorted(votes) # sort votes
    majority = votes[0] # first vote is majority
    maxCount = 0 # max number of votes for a candidate
    count = 0 # number of votes for current candidate
    for vote in votes: # count votes
        if vote == majority: # if vote is for majority
            count += 1 # add vote
            if count > maxCount: # if candidate has more votes than max
                maxCount = count # update max
        else: # vote is not for majority
            majority = vote # update majority
            count = 1 # reset count
    if maxCount > len(votes)/2: # if majority has more than half of votes
        return majority # return majority
    return "Runoff!" # return runoff

def main(pname):
    sys.stdin = open(pname + '.in', 'r') # input
    sys.stdout = open(pname + '.out', 'w') # output

    votes = []
    while True:
        line = input() # get line
        if line == "***": # if votes are over
            break
        votes.append(line) # add vote
    print(getMajority(votes)) # print result

if __name__ == "__main__":
    main('vote') # run main
