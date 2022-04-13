

import sys
import math


def get_score(sven, friends, rounds, friends_num):
    score = 0
    for i in range(rounds):
        for j in range(friends_num):
            if sven[i] == 'S':
                if friends[j][i] == 'P':
                    score += 1
                elif friends[j][i] == 'R':
                    score += 2
            elif sven[i] == 'P':
                if friends[j][i] == 'R':
                    score += 1
                elif friends[j][i] == 'S':
                    score += 2
            elif sven[i] == 'R':
                if friends[j][i] == 'S':
                    score += 1
                elif friends[j][i] == 'P':
                    score += 2
    return score

def get_max_score(sven, friends, rounds, friends_num):
    max_score = 0
    for i in range(rounds):
        for j in range(friends_num):
            if sven[i] == 'S':
                if friends[j][i] == 'R':
                    max_score += 2
                elif friends[j][i] == 'P':
                    max_score += 1
            elif sven[i] == 'P':
                if friends[j][i] == 'S':
                    max_score += 2
                elif friends[j][i] == 'R':
                    max_score += 1
            elif sven[i] == 'R':
                if friends[j][i] == 'P':
                    max_score += 2
                elif friends[j][i] == 'S':
                    max_score += 1
    return max_score

def main():
    rounds = int(input())
    sven = str(input())
    friends_num = int(input())
    friends = ['']*friends_num
    for i in range(friends_num):
        friends[i] = str(input())
    score = get_score(sven, friends, rounds, friends_num)
    max_score = get_max_score(sven, friends, rounds, friends_num)
    print(score)
    print(max_score)

if __name__ == "__main__":
    main()
