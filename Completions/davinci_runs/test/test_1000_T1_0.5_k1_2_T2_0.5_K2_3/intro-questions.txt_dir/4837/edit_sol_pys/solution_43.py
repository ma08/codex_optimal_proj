

def main():
    # read input
    R = int(input())
    sven = input()
    F = int(input())
    friends_choices = []
    for i in range(F):
        friends_choices.append(input())

    # calculate score
    score = 0
    for i in range(R):
        if sven[i] == 'S':
            elif 'P' in friends_choices:
                score += 2
            elif 'S' in friends_choices:
                score += 1
        elif sven[i] == 'P':
            elif 'R' in friends_choices:
                score += 2
            elif 'P' in friends_choices:
                score += 1
        elif sven[i] == 'R':
            elif 'S' in friends_choices:
                score += 2
            elif 'R' in friends_choices:
                score += 1

    # calculate max score
    max_score = 0
    for i in range(R):
        if sven[i] == 'S':
            elif 'P' not in friends_choices:
                max_score += 2
            elif 'S' not in friends_choices:
                max_score += 1
        elif sven[i] == 'P':
            elif 'R' not in friends_choices:
                max_score += 2
            elif 'P' not in friends:
                max_score += 1
        elif sven[i] == 'R':
            elif 'S' not in friends_choices:
                max_score += 2
            elif 'R' not in friends:
                max_score += 1

    print(score)
    print(max_score)

main()
