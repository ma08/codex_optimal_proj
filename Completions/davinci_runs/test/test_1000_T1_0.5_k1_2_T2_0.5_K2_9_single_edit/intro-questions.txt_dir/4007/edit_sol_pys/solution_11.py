

n = int(input())
friends = list(map(int, input().split()))

# Assign gifts to friends who don't have one
i = 1
while i <= n:
    if friends[i - 1] == 0:
        j = i + 1
        while friends[j - 1] != 0:
            j += 1
        friends[i - 1] = j
        friends[j - 1] = i
    i += 1

# Assign gifts to friends who don't have one
j = 1
while j <= n:
    if friends[j - 1] == 0:
        friends[j - 1] = i + 1
        i += 1
    j += 1

# Print out the friends
print(*friends)
