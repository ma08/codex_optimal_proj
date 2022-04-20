

# Read input
n, k = map(int, input().split())
h = list(map(int, input().split()))

# Count people over K
count = 0
for i in h:
    if i >= k:
        count += 1

# Print number of people that can ride
print(count)