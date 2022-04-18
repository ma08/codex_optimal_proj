
import sys

def main():
    rounds = int(sys.stdin.readline().strip())
    sven_seq = sys.stdin.readline().strip()
    friends = int(sys.stdin.readline().strip())

    sven_score = 0
    sven_max_score = 0
    for i in range(friends):
        friend = sys.stdin.readline().strip()
        sven_score += compare(sven_seq, friend)
        sven_max_score += max_compare(sven_seq, friend)
    print(sven_score)
    print(sven_max_score)

def compare(sven_seq, friend):
    score = 0
    for i in range(len(sven_seq)):
        if sven_seq[i] == friend[i]:
            score += 1
        elif sven_seq[i] == "R" and friend[i] == "S":
            score += 2
        elif sven_seq[i] == "S" and friend[i] == "P":
            score += 2
        elif sven_seq[i] == "P" and friend[i] == "R":
            score += 2
    return score

def max_compare(sven_seq, friend):
    score = 0
    for i in range(len(sven_seq)):
        if sven_seq[i] == friend[i]:
            score += 1
        elif sven_seq[i] == "R" and friend[i] == "S":
            score += 2
        elif sven_seq[i] == "S" and friend[i] == "P":
            score += 2
        elif sven_seq[i] == "P" and friend[i] == "R":
            score += 2
        elif sven_seq[i] == "R" and friend[i] == "P":
            score += 0
        elif sven_seq[i] == "S" and friend[i] == "R":
            score += 0
        elif sven_seq[i] == "P" and friend[i] == "S":
            score += 0
    return score

if __name__ == '__main__':
    main()
