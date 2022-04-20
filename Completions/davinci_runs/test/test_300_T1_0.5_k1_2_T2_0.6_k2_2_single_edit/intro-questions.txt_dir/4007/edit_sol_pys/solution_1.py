
n = int(input())
friends = list(map(int, input().split()))

# Find the first friend who doesn't have a gift
i = 1
while i <= n:
    if friends[i - 1] == 0:
        break
    i += 1

# Assign gifts to friends without one
j = 1
while j <= n:
    if friends[j - 1] != 0:
        friends[j - 1] = i
        i += 1
    j += 1

# Print out the friends
print(*friends)
