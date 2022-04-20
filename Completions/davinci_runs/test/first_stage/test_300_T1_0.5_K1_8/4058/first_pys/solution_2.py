

n, r = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

# If there are no heaters, then it is impossible to warm up the whole house
if sum(a) == 0:
    print(-1)
    exit()

# If the heater is at position 0 or n, then we can't warm up the first or last element
if a[0] == 0 or a[-1] == 0:
    print(-1)
    exit()

# Count the number of heaters that need to be turned on
count = 0
for i in range(n):
    # If the current element is not a heater, then add 1 to the count
    if a[i] == 0:
        count += 1

        # If the heater is at position 0 or n, then we can't warm up the first or last element
        if i == 0 or i == n-1:
            print(-1)
            exit()

        # If a heater is at position i-r, then we don't need to turn on the heater at position i
        if a[i-r] == 1:
            count -= 1

print(count)