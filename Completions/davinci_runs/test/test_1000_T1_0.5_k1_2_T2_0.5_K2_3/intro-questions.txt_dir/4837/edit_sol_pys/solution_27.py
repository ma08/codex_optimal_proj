

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
            if 'P' in friends_choices:
                score += 2
            elif 'S' in friends_choices:
                score += 1
        elif sven[i] == 'P':
            if 'R' in friends_choices:
                score += 2
            elif 'P' in friends_choices:
                score += 1
        elif sven[i] == 'R':
            if 'S' in friends_choices:
                score += 2
            elif 'R' in friends_choices:
                score += 1

    # calculate max score
    max_score = 0
    for i in range(R):
        if sven[i] == 'S':
            if 'P' not in friends_choices[i]:
                max_score += 2
            elif 'S' not in friends_choices[i]:
                max_score += 1
        elif sven[i] == 'P':
            if 'R' not in friends_choices[i]:
                max_score += 2
            elif 'P' not in friends_choices[i]:
                max_score += 1
        elif sven[i] == 'R':
            if 'S' not in friends_choices[i]:
                max_score += 2
            elif 'R' not in friends_choices[i]:
                max_score += 1

    print(score)
    print(max_score)

main()
