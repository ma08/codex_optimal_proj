
import sys

def get_majority(votes):
    votes = sorted(votes)
    majority = votes[0]
    maxCount = 0
    count = 0
    for vote in votes:
        if vote == majority:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            majority = vote
            count = 1
    if maxCount > len(votes)/2:
        return majority
    return "Runoff!"

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    votes = []
    while True:
        line = input()
        if line == "***":
            break
        votes.append(line)
    print(get_majority(votes))

if __name__ == "__main__":
    main('vote')
