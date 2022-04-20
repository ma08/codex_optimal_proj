
# SOLUTION

    # min_wins = 0
    # max_wins = 0
    # for i in range(3):
    #     wins = min(a[i], b[(i+1)%3])
    #     min_wins += wins
    #     max_wins += wins
    #     a[i] -= wins
    #     b[(i+1)%3] -= wins
    # max_wins += min(a[0], b[0])
    # return min_wins, max_wins

def rockPaperScissors(n, a, b):
    min_wins = 0
    max_wins = 0
    for i in range(n):
        if a[i] == b[i]:
            continue
        elif a[i] == "R":
            if b[i] == "P":
                min_wins += 1
            else:
                max_wins += 1
        elif a[i] == "P":
            if b[i] == "S":
                min_wins += 1
            else:
                max_wins += 1
        elif a[i] == "S":
            if b[i] == "R":
                min_wins += 1
            else:
                max_wins += 1
    return min_wins, max_wins

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*rockPaperScissors(n, a, b))
