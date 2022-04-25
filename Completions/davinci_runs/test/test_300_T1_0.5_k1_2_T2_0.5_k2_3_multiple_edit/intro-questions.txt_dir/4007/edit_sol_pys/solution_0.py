

n = int(input("Enter number of friends: "))
friends = list(map(int, input("Enter gifts: ").split()))

# Find the first friend who has a gift 
i = 0
while friends[i] != 0:
    i += 1

# Assign gifts to friends who don't have one
j = 1
while j <= n:
    if friends[j - 1] == 0:
        friends[j - 1] = i + 1
        i += 1
    j += 1

# Print out the friends
print("Gifts: ", *friends)
