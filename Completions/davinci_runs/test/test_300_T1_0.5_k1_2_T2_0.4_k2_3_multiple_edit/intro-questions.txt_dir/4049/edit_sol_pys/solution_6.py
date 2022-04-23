

def main():
    # get input
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    # get min/max wins for each game
    min_wins = 0
    max_wins = 0
    for i in range(n):
        if a[i] == b[i]:
            continue
        elif (a[i] + 1) % 3 == b[i]:
            min_wins += 1
            max_wins += 1
        else:
            min_wins += 0
            max_wins += 1
    
    # print result
    print(min_wins, max_wins)

if __name__ == "__main__":
    main()
