
# Read input
n, m = map(int, input().split())  # n = number of items, m = number of voters
votes = list(map(int, input().split()))  # votes for each item

# Check if the most popular item has enough votes
if max(votes) >= (sum(votes) / (4 * m)):
    print("Yes")
else:
    print("No")
