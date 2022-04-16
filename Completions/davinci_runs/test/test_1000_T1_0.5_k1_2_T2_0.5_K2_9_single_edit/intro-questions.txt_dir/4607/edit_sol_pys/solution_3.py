

# Get input for number of test cases
a = int(input())

# Iterate through test cases
for i in range(a):
    # Get input for number of students and threshold
    b,c = map(int, input().split())

# Iterate through months
for month in range(1, a+1):
    # Iterate through days
    for day in range(1, b+1):
        # Increment counter if month and day are equal
        if month == day:
            count += 1

# Print result
print(count)
