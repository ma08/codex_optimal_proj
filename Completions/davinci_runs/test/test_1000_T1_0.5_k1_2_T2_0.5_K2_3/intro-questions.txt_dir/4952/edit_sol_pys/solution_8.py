import collections
import sys

def main():
    votes = []
    for line in sys.stdin:
        if line.strip() == "***":
            break
        votes.append(line.strip())
    vote_dict = collections.defaultdict(int)
    for vote in votes:
        vote_dict[vote] += 1
    max_votes = max(vote_dict.values())
    if max_votes > len(votes) / 2:
        print([name for name, count in vote_dict.items()
               if count == max_votes][0])
    else:
        print("Runoff!")

if __name__ == '__main__':
    main()
