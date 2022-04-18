import sys
import math

def main():
    rounds = int(sys.stdin.readline())
    sven = sys.stdin.readline().strip() # Sven's symbols
    friends = int(sys.stdin.readline())
    friends_symbols = []
    for i in range(friends):
        friends_symbols.append(sys.stdin.readline().strip()) # Friends' symbols
    actual_score = 0 # Score where Sven and his friends play
    largest_score = 0 # Score where Sven plays alone
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
        if sven[i] == "R":
            actual_score += rock # Sven beats rock
            largest_score += friends - max(rock, paper, scissors) # Sven beats all
        elif sven[i] == "P":
            actual_score += paper # Sven beats paper
            largest_score += friends - max(rock, paper, scissors) # Sven beats all
        else:
            actual_score += scissors # Sven beats scissors
            largest_score += friends - max(rock, paper, scissors) # Sven beats all
    print(actual_score)
    print(actual_score + largest_score)

if __name__ == "__main__":
    main()
