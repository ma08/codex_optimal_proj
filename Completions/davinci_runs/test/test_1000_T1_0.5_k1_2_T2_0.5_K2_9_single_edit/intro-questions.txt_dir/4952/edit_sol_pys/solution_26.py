
import sys
from collections import defaultdict

def main():
    votes = defaultdict(int)
    for line in sys.stdin:
        if line == "***\n":
            break
        votes[line.strip("\n")] += 1
    total = sum(votes.values())
    max_vote = max(votes.values())
    if max_vote > total / 2:
        for key, value in votes.items():
            if value == max_vote:
                print(key)
                break
    else:
        print("Runoff!")

if __name__ == '__main__':
    main()
