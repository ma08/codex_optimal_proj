#!/usr/bin/env python3


import sys, collections

def main():
    votes = {}
    for line in sys.stdin:
        if line.strip() == '***':
            break
        votes[line.strip()] = votes.get(line.strip(), 0) + 1

    max_votes = collections.Counter(votes).most_common(1)[0][1]
    if collections.Counter(votes).most_common(2)[0][1] == collections.Counter(votes).most_common(2)[1][1]:
        print('Runoff!')
        return
    else:
        for name, num in collections.Counter(votes).most_common():
            if num == max_votes:
                print(name)
                return

if __name__ == '__main__':
    main()
