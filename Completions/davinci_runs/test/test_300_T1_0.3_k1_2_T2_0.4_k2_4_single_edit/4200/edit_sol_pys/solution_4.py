

# Read input from STDIN
n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Check if the most popular item has enough votes to win
if max(votes) >= (sum(votes) / (4 * m)):
    print("Yes")
else:
    print("No")
