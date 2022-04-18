
import sys

def main():
    rounds = int(sys.stdin.readline().strip())
    sven = sys.stdin.readline().strip()[:rounds]
    friends = int(sys.stdin.readline().strip())
    max_score = 2 * rounds
    score = 0
    for i in range(friends):
        friend = sys.stdin.readline().strip()[:rounds]
        for j in range(len(friend)):
            if sven[j] == friend[j] and friend[j] == "R":
                score += 2 * rounds
            elif sven[j] == friend[j] and friend[j] == "S":
                score += 2 * rounds - 1
            elif sven[j] == friend[j] and friend[j] == "P":
                score += 2 * rounds - 2
            elif (sven[j] == "R" and friend[j] == "S") or (sven[j] == "S" and friend[j] == "P") or (sven[j] == "P" and friend[j] == "R"):
                score += 2 * rounds - 3
        max_score += 2 * rounds - 2
        print(str(score) + "/" + str(max_score))
        score = 0

if __name__ == "__main__":
    main()
