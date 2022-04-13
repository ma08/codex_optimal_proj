import collections
import sys

def main():
    votes = []
    for line in sys.stdin:
        if line.strip() == "***":
            break
        votes.append(line.strip())
    vote_dict = collections.defaultdict(int)  # creates a dictionary with a default value of 0 for all keys
    for vote in votes:
        vote_dict[vote] += 1  # adds 1 to the value of vote in the dictionary
    max_votes = max(vote_dict.values())  # finds the maximum value in the dictionary
    if max_votes > len(votes) / 2:  # checks if there is a majority
        print([name for name, count in vote_dict.items() if count == max_votes][0])  # prints the name of the candidate with the max votes
    else:
        print("Runoff!")

if __name__ == '__main__':
    main()
