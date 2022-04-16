

def main():
    # read input
    R = int(input())
    sven = input()
    N = int(input())
    friends = []
    for i in range(N):
        friends.append(input())

    # calculate score
    score = 0
    for i in range(R):
        if sven[i] == 'S':
            for friend in friends:
                if friend == 'P':
                    score += 2
                elif friend == 'S':
                    score += 1
        elif sven[i] == 'P':
            if 'R' in friends:
                score += 2
            elif 'P' in friends:
                score += 1
        elif sven[i] == 'R':
            if 'S' in friends:
                score += 2
            elif 'R' in friends:
                score += 1

    # calculate max score
    max_score = 0
    for i in range(R):
        if sven[i] == 'S':
            if 'P' not in friends:
                max_score += 2
            elif 'S' not in friends:
                max_score += 1
        elif sven[i] == 'P':
            if 'R' not in friends:
                max_score += 2
            elif 'P' not in friends:
                max_score += 1
        elif sven[i] == 'R':
            if 'S' not in friends:
                max_score += 2
            elif 'R' not in friends:
                max_score += 1

    print(score)
    print(max_score)

main()
