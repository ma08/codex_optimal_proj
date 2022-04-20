

N, M = map(int, input().split())
votes = list(map(int, input().split()))

votes.sort(reverse=True)

for i in range(M):
    if votes[i] < int(sum(votes)/(4*M)):
        print("No")
        exit()
print("Yes")