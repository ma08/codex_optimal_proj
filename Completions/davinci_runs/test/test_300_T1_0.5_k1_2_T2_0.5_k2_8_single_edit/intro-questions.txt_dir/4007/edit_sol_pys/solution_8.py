
n = int(input())
friends = list(map(int, input().split()))

# Assign gifts to friends who don't have one
for i in range(n):
    if friends[i] == 0:
        for j in range(n):
            if friends[j] != 0:
                friends[i] = j + 1
                break

# Print out the friends
print(*friends)
