#!/usr/bin/env python3

n = int(input())
friends = list(map(int, input().split()))

# Find the first friend who has a gift, starting from the end
i = n
while friends[i - 1] != 0:
    i -= 1

# Assign gifts to friends who don't have one
j = 1
while j < n:
    if friends[j] == 0:
        friends[j] = i
        i += 1
    j += 1    

# Print out the friends
print(*friends)
