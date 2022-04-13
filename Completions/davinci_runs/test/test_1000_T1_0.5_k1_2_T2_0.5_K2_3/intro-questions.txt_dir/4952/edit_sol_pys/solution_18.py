'''
import sys
from collections import defaultdict

def main():
    votes = defaultdict(int)
    for line in sys.stdin:
        if line == "***\n":
            break
        votes[line.strip("\n")] += 1
    total = sum(votes.values())
    winner = max(votes, key=votes.get)
    if votes[winner] > total / 2:
        print(winner)
    else:
        print("Runoff!")

if __name__ == '__main__':
    main()
'''
