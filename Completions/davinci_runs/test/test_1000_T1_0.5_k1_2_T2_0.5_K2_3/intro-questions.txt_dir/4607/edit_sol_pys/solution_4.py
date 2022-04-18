
# Get input
a, b = map(int, input().split())

# Initialize counter
count = 0

# Iterate through the months
for month in range(1, a + 1):
    # Iterate through the days
    for day in range(1, b + 1):
        # Increment counter if month and day are equal
        if month == day:
            count += 1

# Print result
print(count)
