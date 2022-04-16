import sys

def main():
    votes = {}
    for line in sys.stdin:
        if line.strip() == "***":
            break
        name, vote = line.strip().split()
        if name in votes:
            votes[name].append(vote)
        else
            votes[name] = [vote]
    for name in votes:
        vote_dict = {}
        for vote in votes[name]:
            if vote in vote_dict:
                vote_dict[vote] += 1
            else:
                vote_dict[vote] = 1
        max_votes = max(vote_dict.values())
        if max_votes > len(votes[name]) / 2:
            print([name for name, count in vote_dict.items() if count == max_votes][0])
        else:
            print("Runoff!")

if __name__ == '__main__':
    main()
