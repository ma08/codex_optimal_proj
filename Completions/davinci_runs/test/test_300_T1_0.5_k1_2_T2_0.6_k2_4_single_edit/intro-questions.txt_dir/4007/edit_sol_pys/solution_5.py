

n = int(input())
friends = list(map(int, input().split()))

# Find the first friend who doesn't have a gift
i = 0
while friends[i] != i + 1:
    i += 1

# Assign gifts to friends who don't have one
j = 1
while j <= n:
    if friends[j - 1] != j:
        friends[j - 1] = i + 1
        i += 1
    j += 1

# Print out the friends
print(*friends)
