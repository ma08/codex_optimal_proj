
n, m = map(int, input().split())
votes = list(map(int, input().split()))
if max(votes) >= (sum(votes) / (4 * m)):
    print("Yes")
else:
    print("No")
