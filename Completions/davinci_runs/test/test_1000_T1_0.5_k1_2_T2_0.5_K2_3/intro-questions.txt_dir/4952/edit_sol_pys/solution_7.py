import sys
import collections

def main():
    vote_dict = {}
    for line in sys.stdin:
        if line.strip() == '***':
            break
        line = line.strip()
        if line not in vote_dict:
            vote_dict[line] = 1
        else:
            vote_dict[line] += 1

    max_votes = vote_dict.most_common(1)[0][1]
    if vote_dict.most_common(2)[0][1] == vote_dict.most_common(2)[1][1]:
        print('Runoff!')
        return
    else:
        for name, num in vote_dict.most_common():
            if num == max_votes:
                print(name)
                return

if __name__ == '__main__':
    main()
