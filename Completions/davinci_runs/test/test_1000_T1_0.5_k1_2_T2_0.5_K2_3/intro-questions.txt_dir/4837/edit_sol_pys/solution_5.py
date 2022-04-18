import sys

def main():
    rounds = int(sys.stdin.readline())
    sven = sys.stdin.readline().strip()
    opponents = int(sys.stdin.readline())
    opponent_symbols = []
    for i in range(opponents):
        opponent_symbols.append(sys.stdin.readline().strip())
    actual_score = 0
    largest_score = 0
    for i in range(rounds):
        rock = 0
        paper = 0
        scissors = 0
        for j in range(opponents):
            if opponent_symbols[j][i] == "R":
                rock += 1
            elif opponent_symbols[j][i] == "P":
                paper += 1
            else:
                scissors += 1
        if sven[i] == "R":
            actual_score += rock
            largest_score += opponents - max(rock, paper, scissors)
        elif sven[i] == "P":
            actual_score += paper
            largest_score += opponents - max(rock, paper, scissors)
        else:
            actual_score += scissors
            largest_score += opponents - max(rock, paper, scissors)
    print(actual_score)
    print(actual_score + largest_score)

if __name__ == "__main__":
    main()
