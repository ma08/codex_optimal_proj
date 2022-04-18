
import sys

def main():
    votes = []
    for vote in sys.stdin:
        if vote.strip() != '***':
            votes.append(vote.strip())
        else:
            break
    max_votes = 0
    for i in set(votes):
        if votes.count(i) > max_votes:
            max_votes = votes.count(i)
            winner = i
    if max_votes > len(votes)/2:
        print(winner)
    else:
        print('Runoff!')

if __name__ == '__main__':
    main()
