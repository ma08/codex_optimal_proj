

#-----Solution-----

# Read input
n, r = map(int, input().split())
a = list(map(int, input().split()))

# Check if there is a heater
heater = False
for i in a:
    if i == 1:
        heater = True

# If there is no heater, the answer is -1
if not heater:
    print(-1)
    exit()

# If there is a heater, count the number of heaters needed
ans = 0
i = 0
while i < n:
    # If there is no heater at the current position, move to the next position
    if a[i] == 0:
        i += 1
        continue
    # If there is a heater at the current position, move to the next position that is not warmed up by the heater
    if a[i] == 1:
        ans += 1
        i += 2 * r - 1

# Print the answer
print(ans)