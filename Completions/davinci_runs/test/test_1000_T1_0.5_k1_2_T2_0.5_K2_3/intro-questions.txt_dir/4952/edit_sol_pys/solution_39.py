

import sys

def getMajority(votes):
    voteList = sorted(votes)
    majority = voteList[0]
    maxCount = 0
    count = 0
    for vote in voteList:
        if vote == majority:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            majority = vote
            count = 1
    if maxCount > len(voteList)/2:
        return majority
    return "Runoff!"

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    voteList = []
    while True:
        line = input()
        if line == "***":
            break
        voteList.append(line)
    print(getMajority(voteList)) 

if __name__ == "__main__":
    main('vote')
