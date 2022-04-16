

import sys
import math

def main():
    rounds = int(sys.stdin.readline())
    sven = sys.stdin.readline().strip()  # Sven's symbols
    friends = int(sys.stdin.readline())
    friends_symbols = []  # Each friend's symbols
    for i in range(friends):
        friends_symbols.append(sys.stdin.readline().strip())  # Friends' symbols
    actual_score = 0
    largest_score = 0
    for i in range(rounds):
        rock = 0  # Number of rocks
        paper = 0  # Number of papers
        scissors = 0  # Number of scissors
        for j in range(friends):
            if friends_symbols[j][i] == "R":  # If a friend played rock
                rock += 1
            elif friends_symbols[j][i] == "P":
                paper += 1
            else:
                scissors += 1
        if sven[i] == "R":
            actual_score += rock
            largest_score += friends - max(rock, paper, scissors)
        elif sven[i] == "P":
            actual_score += paper
            largest_score += friends - max(rock, paper, scissors)
        else:
            actual_score += scissors
            largest_score += friends - max(rock, paper, scissors)
    print(actual_score)
    print(actual_score + largest_score)

if __name__ == "__main__":
    main()
