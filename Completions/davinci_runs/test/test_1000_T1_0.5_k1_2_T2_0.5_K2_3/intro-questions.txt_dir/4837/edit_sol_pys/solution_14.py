
import sys

def main():
    rounds = int(sys.stdin.readline().strip()) # number of rounds, not used
    sven = sys.stdin.readline().strip()
    friends = int(sys.stdin.readline().strip()) # number of friends

    sven_score = 0
    for i in range(friends):
        friend = sys.stdin.readline().strip()
        sven_score += compare(sven, friend)
    print(sven_score)

def compare(sven, friend):
    score = 0
    for i in range(len(sven)):
        if sven[i] == friend[i]:
            score += 1
        elif sven[i] == "R" and friend[i] == "S":
            score += 2
        elif sven[i] == "S" and friend[i] == "P":
            score += 2
        elif sven[i] == "P" and friend[i] == "R":
            score += 2
    return score

if __name__ == '__main__':
    main()
