

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
            for j in range(N):
                if Friends[j][i] == 'P':
                    Score += 2
                    break
                elif Friends[j][i] == 'S':
                    Score += 1
                    break
        elif Sven[i] == 'P':
            for j in range(N):
                if Friends[j][i] == 'R':
                    Score += 2
                    break
                elif Friends[j][i] == 'P':
                    Score += 1
                    break
        elif Sven[i] == 'R':
            if 'S' in Friends:
                Score += 2
            elif 'R' in Friends:
                Score += 1

    # calculate max score
    Max_score = 0
    for i in range(R):
        if Sven[i] == 'S':
            if 'P' not in Friends:
                Max_score += 2
            elif 'S' not in Friends:
                Max_score += 1
        elif Sven[i] == 'P':
            if 'R' not in Friends:
                Max_score += 2
            elif 'P' not in Friends:
                Max_score += 1
        elif Sven[i] == 'R':
            if 'S' not in Friends:
                Max_score += 2
            elif 'R' not in Friends:
                Max_score += 1

    print(Score)
    print(Max_score)

main()
