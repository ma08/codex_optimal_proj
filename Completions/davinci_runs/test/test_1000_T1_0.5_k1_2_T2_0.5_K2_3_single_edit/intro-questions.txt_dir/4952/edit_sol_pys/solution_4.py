
import sys


def main():
    line = sys.stdin.readline()
    while line:
        votes = []
        while line and line.strip() != "***":
            votes.append(line.strip())
            line = sys.stdin.readline()
        vote_dict = {}
        for vote in votes:
            if vote in vote_dict:
                vote_dict[vote] += 1
            else:
                vote_dict[vote] = 1
        max_votes = max(vote_dict.values())
        if max_votes > len(votes) / 2:
            print([name for name, count in vote_dict.items() if count == max_votes][0])
        else:
            print("Runoff!")
        line = sys.stdin.readline()


if __name__ == '__main__':
    main()
