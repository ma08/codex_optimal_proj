

def main():
    # get input
    n = int(input()) # number of rounds
    a = [int(x) for x in input().split()] # a's moves per round
    b = [int(x) for x in input().split()] # b's moves per round
    
    # get min/max
    min_wins = 0
    max_wins = 0
    for i in range(3): # loop through rock, paper, scissor
        for j in range(3): # loop through rock, paper, scissor
            if i == j:
                continue
            elif (i + 1) % 3 == j:
                min_wins += min(a[i], b[j])
                max_wins += max(a[i], b[j])
            else:
                min_wins += max(a[i], b[j])
                max_wins += min(a[i], b[j])
    
    # print result
    print(min_wins, max_wins)

if __name__ == "__main__":
    main()
