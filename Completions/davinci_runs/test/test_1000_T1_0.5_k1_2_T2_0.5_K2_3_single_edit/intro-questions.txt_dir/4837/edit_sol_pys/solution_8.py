import sys

def main():
    rounds = int(sys.stdin.readline().strip())
    sven = sys.stdin.readline().strip()
    friends = int(sys.stdin.readline().strip())
    max_score = 2 * rounds
    score = 0
    for i in range(friends):
        friend = sys.stdin.readline().strip()
        for j in range(rounds):
            if sven[j] == friend[j]:
                score += 1
            elif (sven[j] == "R" and friend[j] == "S") or (sven[j] == "S" and friend[j] == "P") or (sven[j] == "P" and friend[j] == "R"):
                score += 2
        print(score)
        print(max_score)
        score = 0
        max_score = 2 * rounds

if __name__ == "__main__":
    main()
