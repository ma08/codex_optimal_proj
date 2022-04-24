

n, m = (int(x) for x in input().split())
votes = [int(x) for x in input().split()]
votes.sort()

total_votes = sum(votes)

if votes[m - 1] >= (total_votes / (4 * m)):
    print("Yes")
else:
    print("No")
