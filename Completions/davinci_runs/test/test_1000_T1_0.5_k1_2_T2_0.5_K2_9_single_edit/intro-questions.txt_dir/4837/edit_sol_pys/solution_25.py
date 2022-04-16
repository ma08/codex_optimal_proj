

import sys
import math


def get_score(sven, friends):
    if len(sven) != len(friends[0]):
        print('Error: Sven and friends have different numbers of rounds')
        return -1
    else:
        rounds = len(sven)
    score = 0
    for i in range(len(sven)):
        if sven[i] == 'S':
            if friends[i] == 'P':
                score += 1
            elif friends[i] == 'R':
                score += 2
        elif sven[i] == 'P':
            if friends[i] == 'R':
                score += 1
            elif friends[i] == 'S':
                score += 2
        elif sven[i] == 'R':
            if friends[i] == 'S':
                score += 1
            elif friends[i] == 'P':
                score += 2
    return score

def get_max_score(sven, friends):
    max_score = 0
    for i in range(len(sven)):
        if sven[i] == 'S':
            if friends[i] == 'R':
                max_score += 2
            elif friends[i] == 'P':
                max_score += 1
        elif sven[i] == 'P':
            if friends[i] == 'S':
                max_score += 2
            elif friends[i] == 'R':
                max_score += 1
        elif sven[i] == 'R':
            if friends[i] == 'P':
                max_score += 2
            elif friends[i] == 'S':
                max_score += 1
    return max_score


def main():
    rounds = int(input())
    sven = str(input())
    friends_num = int(input())
    friends = []
    for i in range(friends_num):
        friends.append(str(input()))
    score = get_score(sven, friends)
    max_score = get_max_score(sven, friends)
    print(score)
    print(max_score)

if __name__ == "__main__":
    main()
