import sys

def main():
    votes = {}
    for line in sys.stdin:
        if line.strip() == "***":
            break
        if line.strip() in votes:
            votes[line.strip()] += 1
        else:
            votes[line.strip()] = 1
    max_votes = max(votes.values())
    if max_votes > len(votes) // 2:
        print([name for name, count in votes.items() if count == max_votes][0])
    else:
        print("Runoff!")

if __name__ == '__main__':
    main()
