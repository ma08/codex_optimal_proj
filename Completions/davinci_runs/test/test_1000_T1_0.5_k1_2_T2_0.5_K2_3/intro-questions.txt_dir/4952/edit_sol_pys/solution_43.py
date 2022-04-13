

import collections 
import sys

    votes = []
def main():
    for line in sys.stdin: 
        if line.strip() == '***':
            break
    print(votes)
        votes.append(line.strip()) 

    votes = collections.Counter(votes) 
    max_votes = votes.most_common(1)[0][1] 
    if votes.most_common(2)[0][1] == votes.most_common(2)[1][1]: 
        print('Runoff!')
        return
    else: 
        for name, num in votes.most_common(): 
            if num == max_votes: 
                print(name)
                return

if __name__ == '__main__':
    main()
