
# Get the input 
d, m = map(int, input().strip().split())

# Define the days of the week
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

# Define the number of days in each month
daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Define the number of days since the first of January
totalDays = 0

# Loop through each of the months and add the number of days to the total
for i in range(m - 1):
    totalDays += daysInMonths[i]

# Add the days to the total
totalDays += d

# Print the day of the week
print(days[(totalDays + 3) % 7])
