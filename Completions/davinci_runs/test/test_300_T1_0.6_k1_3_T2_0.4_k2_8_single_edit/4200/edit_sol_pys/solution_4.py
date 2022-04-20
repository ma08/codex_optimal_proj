
n, m = (int(x) for x in input().split())
votes = [int(x) for x in input().split()]
votes.sort()
votes.reverse()

total_votes = sum(votes)

print("Yes" if votes[0] >= (total_votes / (4 * m)) else "No")
