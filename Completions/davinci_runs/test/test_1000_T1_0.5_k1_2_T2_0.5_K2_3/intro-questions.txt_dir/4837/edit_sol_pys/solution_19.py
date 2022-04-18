

import sys
import math

def main():
    rounds = int(sys.stdin.readline())
    sven_symbols = sys.stdin.readline().strip()
    friends = int(sys.stdin.readline())
    friends_symbols = []
    for i in range(friends):
        friends_symbols.append(sys.stdin.readline().strip())
    actual_score = 0
    largest_score = 0
    for i in range(rounds):
        rock = 0
        paper = 0
        scissors = 0
        for j in range(friends):
            if friends_symbols[j][i] == "R":
                rock += 1
            elif friends_symbols[j][i] == "P":
                paper += 1
            else:
                scissors += 1
        if sven_symbols[i] == "R":
            actual_score += rock
            largest_score += friends - max(rock, paper, scissors)
        elif sven_symbols[i] == "P":
            actual_score += paper
            largest_score += friends - max(rock, paper, scissors)
        else:
            actual_score += scissors
            largest_score += friends - max(rock, paper, scissors)
    print(actual_score)
    print(int(actual_score + largest_score))

if __name__ == "__main__":
    main()
