

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
                    break
                elif friend == 'S':
                    score += 1
                    break
        elif sven[i] == 'P':
            for friend in friends:
                if friend == 'R':
                    score += 2
                    break
                elif friend == 'P':
                    score += 1
                    break
        elif sven[i] == 'R':
            for friend in friends:
                if friend == 'S':
                    score += 2
                    break
                elif friend == 'R':
                    score += 1
                    break

    # calculate max score
    max_score = 0
    for i in range(R):
        if sven[i] == 'S':
            for friend in friends:
                if friend == 'P':
                    max_score += 1
                    break
                elif friend == 'S':
                    max_score += 0
                    break
            else:
                max_score += 2
        elif sven[i] == 'P':
            for friend in friends:
                if friend == 'R':
                    max_score += 1
                    break
                elif friend == 'P':
                    max_score += 0
                    break
            else:
                max_score += 2
        elif sven[i] == 'R':
            for friend in friends:
                if friend == 'S':
                    max_score += 1
                    break
                elif friend == 'R':
                    max_score += 0
                    break
            else:
                max_score += 2

    print(score)
    print(max_score)

main()
