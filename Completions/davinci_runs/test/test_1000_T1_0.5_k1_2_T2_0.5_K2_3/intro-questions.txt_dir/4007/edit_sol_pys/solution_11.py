

n = int(input())
friends = list(map(int, input().split()))

# Check if the first friend is 0
if friends[0] == 0:
    i = 1
else:
    i = 0

# Assign gifts to friends who don't have one
while i < n:
    if friends[i] == 0:
        friends[i] = i + 1
    i += 1

# Print out the friends
print(*friends)
