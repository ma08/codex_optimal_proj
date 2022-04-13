
n = int(input())
friends = list(map(int, input().split()))

# Find the first friend who has a gifts
i = 0
while friends[i] != 0:
    i += 1

# Assign gifts to friends who don't have ones
j = 1
while j <= n:
    if friends[j - 1] == 0:
        friends[j - 1] = i + 1
        i += 1
    j += 1

# Print out the friends
print(*friends)
