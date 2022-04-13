

# Get input from user
a, b = map(int, input().split())

# Initialize a counter
count = 0

# Iterate through the months 1 to a
for month in range(1, a+1):
    # Iterate through the days 1 to b
    for day in range(1, b+1):
        # Increment count if month and day are equal
        if month == day:
            count += 1

# Print result
print(count)
