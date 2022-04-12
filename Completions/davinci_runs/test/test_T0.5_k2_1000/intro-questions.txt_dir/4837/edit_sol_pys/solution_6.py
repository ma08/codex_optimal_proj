

def main():
    # read input
    R = int(input())
    Sven = input()
    N = int(input())
    Friends = []
    for i in range(N):
        Friends.append(input())

    # calculate score
    Score = 0
    for i in range(R):
        if Sven[i] == 'S':
            if 'P' in Friends[i]:
                Score += 2
            elif 'S' in Friends[i]:
                Score += 1
        elif Sven[i] == 'P':
            if 'R' in Friends[i]:
                Score += 2
            elif 'P' in Friends[i]:
                Score += 1
        elif Sven[i] == 'R':
            if 'S' in Friends[i]:
                Score += 2
            elif 'R' in Friends[i]:
                Score += 1

    # calculate max score
    Max_score = 0
    for i in range(R):
        if Sven[i] == 'S':
            if 'P' not in Friends[i]:
                Max_score += 2
            elif 'S' not in Friends[i]:
                Max_score += 1
        elif Sven[i] == 'P':
            if 'R' not in Friends[i]:
                Max_score += 2
            elif 'P' not in Friends[i]:
                Max_score += 1
        elif Sven[i] == 'R':
            if 'S' not in Friends[i]:
                Max_score += 2
            elif 'R' not in Friends[i]:
                Max_score += 1

    print(Score)
    print(Max_score)

main()
