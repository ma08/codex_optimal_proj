

# Get the number of days
d = int(input().strip())

# Get the number of months
m = int(input().strip())

# Define the number of days in each month
daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Define the number of days since the first of January
total_days = 0

# Loop through each of the months and add the number of days to the total
for i in range(m - 1):
    total_days += daysInMonths[i]

# Add the days to the total
total_days += d

# Print the day of the week
print(days[(total_days + 3) % 7])
