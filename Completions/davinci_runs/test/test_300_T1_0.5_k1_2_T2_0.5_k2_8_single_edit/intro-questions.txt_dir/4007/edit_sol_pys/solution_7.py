n = int(input())
a = list(map(int, input().split()))


# Find the first friend who has a gift
i = 0
while a[i] != 0:
    i += 1

# Assign gifts to friends who don't have one
j = 1
while j <= n:
    if a[j - 1] == 0:
        a[j - 1] = i + 1
        i += 1
    j += 1

# Print out the friends' gifts
print(*a)
