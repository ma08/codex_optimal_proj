

n = int(input())
arr = list(map(int, input().split()))

# Find the first friend who has a gift
i = 0
while arr[i] != 0:
    i += 1

# Assign gifts to friends who don't have one
j = 1
while j <= n:
    if arr[j - 1] == 0:
        arr[j - 1] = i + 1
        i += 1
    j += 1

# Print out the friends
print(*arr)
