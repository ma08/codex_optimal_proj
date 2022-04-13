
import sys

def main():
    rounds = int(sys.stdin.readline().strip())  # number of rounds
    sven = sys.stdin.readline().strip()
    friends = int(sys.stdin.readline().strip())  # number of friends

    sven_score = 0
    sven_max_score = 0
    for i in range(friends):
        friend = sys.stdin.readline().strip()
        sven_score += compare(sven, friend)
        sven_max_score += max_compare(sven, friend)
    print(sven_score)

    print(sven_max_score)

def compare(sven, friend):
    score = 0
    for i in range(len(sven)):
        if sven[i] == friend[i]:
            score += 1
        elif sven[i] == "R" and friend[i] == "S" or sven[i] == "S" and friend[i] == "P" or sven[i] == "P" and friend[i] == "R":
            score += 2

    return score


def max_compare(sven, friend):
    score = 0
    for i in range(len(sven)):
        if sven[i] == friend[i]:
            score += 1
        elif sven[i] == "R" and friend[i] == "S" or sven[i] == "S" and friend[i] == "P" or sven[i] == "P" and friend[i] == "R":
            score += 2

    return score


if __name__ == '__main__':
    main()
