

def main():
    # get input
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    # get min/max wins
    min_wins = 0
    max_wins = 0
    min_wins += min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    max_wins += max(a[0], b[1]) + max(a[1], b[2]) + max(a[2], b[0])
    
    # print result
    print(min_wins, max_wins)

if __name__ == "__main__":
    main()
