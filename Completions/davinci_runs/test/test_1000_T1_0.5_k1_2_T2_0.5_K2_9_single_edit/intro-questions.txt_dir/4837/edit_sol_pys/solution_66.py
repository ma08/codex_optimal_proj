

import sys
import math

def main():
    rounds = int(sys.stdin.readline())
    sven = sys.stdin.readline().strip()  # readline() reads a line from the file and strip() removes the newline
    friends = int(sys.stdin.readline())
    friends_symbols = []  # create a list of friends' symbols
    for i in range(friends):
        friends_symbols.append(sys.stdin.readline().strip())  # append the list with friends' symbols
    actual_score = 0
    largest_score = 0
    for i in range(rounds):  # for each round
        rock = 0
        paper = 0
        scissors = 0
        for j in range(friends):  # for each friend
            if friends_symbols[j][i] == "R":  # if the friend plays rock
                rock += 1
            elif friends_symbols[j][i] == "P":  # if the friend plays paper
                paper += 1
            else:
                scissors += 1  # if the friend plays scissors
        if sven[i] == "R":  # if Sven plays rock
            actual_score += rock
            largest_score += friends - max(rock, paper, scissors)  # the largest possible score in this round
        elif sven[i] == "P":  # if Sven plays paper
            actual_score += paper
            largest_score += friends - max(rock, paper, scissors)  # the largest possible score in this round
        else:
            actual_score += scissors
            largest_score += friends - max(rock, paper, scissors)  # the largest possible score in this round
    print(actual_score)
    print(actual_score + largest_score)

if __name__ == "__main__":
    main()
