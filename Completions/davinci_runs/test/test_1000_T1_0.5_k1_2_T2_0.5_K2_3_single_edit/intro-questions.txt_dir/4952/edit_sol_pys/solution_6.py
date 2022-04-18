

import sys, os
from collections import defaultdict

def main():
    votes = defaultdict(int)
    for line in open(os.getenv("VOTES")):
        if line == "***":
            break
        votes[line.strip("\n").strip("\r")] += 1
    total = sum(votes.values())
    winner = max(votes, key=votes.get)
    if votes[winner] > total / 2:
        print(winner)
    else:
        print("Runoff!")

if __name__ == '__main__':
    main()
