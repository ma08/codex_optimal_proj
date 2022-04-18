

# Get input from user
a,b = map(int, input().split())

# Initialize counter
count = 0

# Iterate through months and days
for month in range(1, a + 1):
    for day in range(1, b + 1):
        # Check if month and day are equal
        if month == day: count += 1

# Print result
print(count)
