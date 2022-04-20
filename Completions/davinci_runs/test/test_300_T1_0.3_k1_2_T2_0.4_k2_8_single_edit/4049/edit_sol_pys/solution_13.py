
# SOLUTION

def rockPaperScissors(n, a, b):
    min_wins = sum(min(a[i], b[(i+1)%3]) for i in range(3))
    max_wins = sum(min(a[i], b[(i+2)%3]) for i in range(3))
    return min_wins, max_wins + min(a[0], b[0])

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*rockPaperScissors(n, a, b))
