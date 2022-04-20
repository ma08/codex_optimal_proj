

# Read input
n, m = map(int, raw_input().split())
votes = list(map(int, raw_input().split()))

# Check if the most popular item has enough votes
if max(votes) >= (sum(votes) / (4 * m)):
    print("Yes")
else:
    print("No")
