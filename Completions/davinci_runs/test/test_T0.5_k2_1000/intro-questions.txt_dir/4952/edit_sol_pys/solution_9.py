
import sys
import collections

def main():
    votes = []
    for line in sys.stdin:
        if line.strip() == '***':
            break
        votes.append(line.strip())

    vote_count = collections.Counter(votes)
    max_votes = vote_count.most_common(1)[0][1]
    if vote_count.most_common(2)[0][1] == vote_count.most_common(2)[1][1]:
        print('Runoff!')
        return
    else:
        for name, num in vote_count.most_common():
            if num == max_votes:
                print(name)
                return

if __name__ == '__main__':
    main()
