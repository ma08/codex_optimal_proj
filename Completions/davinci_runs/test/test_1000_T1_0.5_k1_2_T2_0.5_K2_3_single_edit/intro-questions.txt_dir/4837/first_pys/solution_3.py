

import sys

def main():
    r = int(sys.stdin.readline().strip())
    sven = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    friends = []
    for i in range(n):
        friends.append(sys.stdin.readline().strip())

    # Actual score
    score = 0
    for i in range(r):
        for friend in friends:
            if sven[i] == 'R':
                if friend[i] == 'S':
                    score += 2
                elif friend[i] == 'P':
                    score += 1
            elif sven[i] == 'S':
                if friend[i] == 'P':
                    score += 2
                elif friend[i] == 'R':
                    score += 1
            elif sven[i] == 'P':
                if friend[i] == 'R':
                    score += 2
                elif friend[i] == 'S':
                    score += 1
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