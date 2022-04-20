

def main():
    # get input
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    # get min/max
    min_wins = 0
    max_wins = 0
        cur_min = 0
        cur_max = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            elif (i + 1) % 3 == j:
                cur_min += min(a[i], b[j])
                cur_max += max(a[i], b[j])
            else:
                cur_min += max(a[i], b[j])
                cur_max += min(a[i], b[j])
        min_wins = max(min_wins, cur_min)
        max_wins = max(max_wins, cur_max)
    
    # print result
    print(min_wins, max_wins)

if __name__ == "__main__":
    main()
