
import sys

def main():
    r = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    friends = []
    for i in range(n):
        friends.append(sys.stdin.readline().strip())

    # Actual score
    score = 0
    for i in range(n):
        for friend in friends:
            if s[i] == 'R':
                if friend[i] == 'S':
                    score += 2
                elif friend[i] == 'P':
                    score += 1
            elif s[i] == 'S':
                if friend[i] == 'P':
                    score += 2
                elif friend[i] == 'R':
                    score += 1
            elif s[i] == 'P':
                if friend[i] == 'R':
                    score += 2
                elif friend[i] == 'S':
                    score += 1
    print(score)

    # Max score
    score = 0
    for i in range(n):
        for friend in friends:
            if s[i] == 'R':
                if friend[i] == 'S':
                    score += 2
            elif s[i] == 'S':
                if friend[i] == 'P':
                    score += 2
            elif s[i] == 'P':
                if friend[i] == 'R':
                    score += 2
    score += r
    print(score)

if __name__ == "__main__":
    main()
