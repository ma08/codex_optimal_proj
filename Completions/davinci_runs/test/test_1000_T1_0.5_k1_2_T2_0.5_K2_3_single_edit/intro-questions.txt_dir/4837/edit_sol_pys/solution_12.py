

def main():
    # read input
    R = int(input())
    sven = input()
    N = int(input())
    friends = set()
    for i in range(N):
        friends.add(input())

    # calculate score
    score = 0
    for i in range(R):
        if sven[i] == 'S':
            if 'P' in friends or 'S' in friends:
                score += 2
        elif sven[i] == 'P':
            if 'R' in friends or 'P' in friends:
                score += 2
        elif sven[i] == 'R':
            if 'S' in friends or 'R' in friends:
                score += 2

    # calculate max score
    max_score = 0
    for i in range(R):
        if sven[i] == 'S':
            if 'P' not in friends:
                max_score += 2
        elif sven[i] == 'P':
            if 'R' not in friends:
                max_score += 2
        elif sven[i] == 'R':
            if 'S' not in friends:
                max_score += 2

    print(score)
    print(max_score)

main()
