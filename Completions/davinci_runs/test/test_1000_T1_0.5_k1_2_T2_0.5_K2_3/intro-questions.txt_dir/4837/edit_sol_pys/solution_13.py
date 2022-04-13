
import sys

def main():
    rounds = int(sys.stdin.readline().strip())
    sven = sys.stdin.readline().strip()
    friends = int(sys.stdin.readline().strip())
    max_score = 0
    score = 0
    for i in range(friends):
        friend = sys.stdin.readline().strip()
        for j in range(rounds):
            if sven[j] == friend[j]:
                score += 1
            elif (sven[j] == "R" and friend[j] == "S") or (sven[j] == "S" and friend[j] == "P") or (sven[j] == "P" and friend[j] == "R"):
                score += 2
        if score > max_score:
            max_score = score
        print(score)
        score = 0
    print(max_score)

if __name__ == "__main__":
    main()
