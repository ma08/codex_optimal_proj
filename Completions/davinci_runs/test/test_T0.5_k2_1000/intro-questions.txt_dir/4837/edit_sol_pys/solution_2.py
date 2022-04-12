
import sys

def main():
    rounds = int(sys.stdin.readline().strip())
    Sven = sys.stdin.readline().strip()
    friends = int(sys.stdin.readline().strip())

    Sven_score = 0
    Sven_max_score = 0
    for i in range(friends):
        friend = sys.stdin.readline().strip()
        Sven_score += compare(Sven, friend)
        Sven_max_score += max_compare(Sven, friend)
    print(Sven_score)
    print(Sven_max_score)

def compare(Sven, friend):
    score = 0
    for i in range(len(Sven)):
        if Sven[i] == friend[i]:
            score += 1
        elif Sven[i] == "R" and friend[i] == "S":
            score += 2
        elif Sven[i] == "S" and friend[i] == "P":
            score += 2
        elif Sven[i] == "P" and friend[i] == "R":
            score += 2
    return score

def max_compare(Sven, friend):
    score = 0
    for i in range(len(Sven)):
        if Sven[i] == friend[i]:
            score += 1
        elif Sven[i] == "R" and friend[i] == "S":
            score += 2
        elif Sven[i] == "S" and friend[i] == "P":
            score += 2
        elif Sven[i] == "P" and friend[i] == "R":
            score += 2
        elif Sven[i] == "R" and friend[i] == "P":
            score += 0
        elif Sven[i] == "S" and friend[i] == "R":
            score += 0
        elif Sven[i] == "P" and friend[i] == "S":
            score += 0
    return score

if __name__ == '__main__':
    main()
