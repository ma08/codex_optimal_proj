

import sys

def main():
    r = int(sys.stdin.readline().strip())
    svens = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    friends = []
    for i in range(n):
        friends.append(sys.stdin.readline().strip())

    # Actual score
    # score = 0
    # for i in range(r):
    #     for friend in friends:
    #         if svens[i] == 'R':
    #             if friend[i] == 'S':
    #                 score += 2
    #             elif friend[i] == 'P':
    #                 score += 1
    #         elif svens[i] == 'S':
    #             if friend[i] == 'P':
    #                 score += 2
    #             elif friend[i] == 'R':
    #                 score += 1
    #         elif svens[i] == 'P':
    #             if friend[i] == 'R':
    #                 score += 2
    #             elif friend[i] == 'S':
    #                 score += 1
    # print(score)

    # Max score
    score = 0
    for friend in friends:
        for i in range(r):
            if svens[i] == 'R' and friend[i] == 'S':
                score += 2
            elif svens[i] == 'S' and friend[i] == 'P':
                score += 2
            elif svens[i] == 'P' and friend[i] == 'R':
                score += 2
    score += r
    print(score)

if __name__ == "__main__":
    main()
