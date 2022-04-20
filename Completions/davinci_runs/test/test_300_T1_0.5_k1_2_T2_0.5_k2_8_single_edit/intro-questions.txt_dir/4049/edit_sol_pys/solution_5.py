

def main():
    # get input
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    # get min/max
    min_wins = 0
    max_wins = 0
    for i in range(n):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            min_wins += b[i]
            max_wins += a[i]
        else:
            min_wins += a[i]
            max_wins += b[i]
    
    # print result
    print(min_wins, max_wins)

if __name__ == "__main__":
    main()
