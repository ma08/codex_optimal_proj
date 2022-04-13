
#
import sys

def main():
    r = int(sys.stdin.readline().strip())
    sven = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    friends = [None] * n
    for i in range(n):
        friends[i] = list(sys.stdin.readline().strip())

    # Actual score - no cheating
    score = 0
    for i in range(r):
        for friend in friends:
            if sven[i] == 'R' and friend[i] == 'S':
                    score += 2
            elif sven[i] == 'S' and friend[i] == 'P':
                    score += 1
            elif sven[i] == 'P' and friend[i] == 'R':
                    score += 2
    print(score)

    # Max score
    score = 0
    for i in range(r):
        for friend in friends:
            if sven[i] == 'R':
                if friend[i] == 'S':
                    score += 2
            elif sven[i] == 'S':
                if friend[i] == 'P':
                    score += 2
            elif sven[i] == 'P':
                if friend[i] == 'R':
                    score += 2
    score += r
    print(score)

if __name__ == "__main__":
    main()
