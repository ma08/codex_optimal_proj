
import sys

def main():
    rounds = int(sys.stdin.readline().strip())
    sven = sys.stdin.readline().strip()
    friends = int(sys.stdin.readline().strip())
    max_score = 0
    score = 0
    for _ in range(friends):
        friend = sys.stdin.readline().strip()
        for i in range(rounds):
            if sven[i] == friend[i]:
                score += 1
            elif (sven[i] == "R" and friend[i] == "S") or (sven[i] == "S" and friend[i] == "P") or (sven[i] == "P" and friend[i] == "R"):
                score += 2
        max_score = max(max_score, score)
        score = 0 
    print(max_score)

if __name__ == "__main__":
    main()
