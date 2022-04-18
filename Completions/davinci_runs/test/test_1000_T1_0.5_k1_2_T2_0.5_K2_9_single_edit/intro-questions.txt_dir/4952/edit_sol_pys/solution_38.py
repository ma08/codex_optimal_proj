
import sys
from collections import defaultdict

def main():
    votes = defaultdict(int)  # to store the votes
    for line in sys.stdin:
        if line == "***\n":  # end of votes
            break
        votes[line.strip("\n")] += 1  # add vote
    total = sum(votes.values())  # total votes
    winner = max(votes, key=votes.get)  # get the winner
    if votes[winner] > total / 2:  # check if winner won by majority
        print(winner)
    else:
        print("Runoff!")

if __name__ == '__main__':
    main()
