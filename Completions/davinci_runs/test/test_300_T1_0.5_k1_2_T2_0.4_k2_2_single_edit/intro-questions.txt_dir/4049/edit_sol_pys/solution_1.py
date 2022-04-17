

def main():
    # get input
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    # get min/max
    min_wins = 0
    max_wins = 0
    for i in range(n):
        if a[i] > b[i]:
            min_wins += 1
            max_wins += 1
        elif a[i] < b[i]:
            min_wins += 0
            max_wins += 1
        else:
            min_wins += 0
            max_wins += 0
    
    # print result
    print(min_wins, max_wins)

if __name__ == "__main__":
    main()
