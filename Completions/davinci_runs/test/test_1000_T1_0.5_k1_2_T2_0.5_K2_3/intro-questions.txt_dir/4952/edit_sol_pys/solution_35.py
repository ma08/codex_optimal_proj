
import sys

def main():
    votes = []
    for line in sys.stdin:
        if line.strip() != '***':
            votes.append(line.strip())
        else:
            break
    max_votes = 0
    for candidate in set(votes):
        if votes.count(candidate) > max_votes:
            max_votes = votes.count(candidate)
            winner = candidate
    if max_votes > len(votes)/2:
        print(winner)
    else:
        print('Runoff!')
if __name__ == '__main__':
    main()
