

# SOLUTION

def rockPaperScissors(n, a, b, c):
    min_wins = 0
    max_wins = 0
    for i in range(3):
        wins = min(a[i], c[(i+1)%3])
        min_wins += wins
        max_wins += wins
        a[i] -= wins
        c[(i+1)%3] -= wins
    max_wins += min(a[0], c[0])
    return min_wins, max_wins

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
print(*rockPaperScissors(n, a, b, c))
