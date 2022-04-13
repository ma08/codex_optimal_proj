

# First, determine the number of days between the start of 2009 and the input date.
# Then, find the day of the week of the start of 2009.
# Finally, add the number of days to the start of 2009 and output the day of the week.

# Import date time library.
from datetime import date

# Get input
d, m = [int(x) for x in input().split()]

# Calculate the number of days between the start of 2009 and the input date
# Note that this is a negative number
days = date(2009, m, d) - date(2009, 1, 1)

# Find the day of the week of the start of 2009
# Note that this is the day of the week of the input date
days = days.days % 7

# Add the number of days to the start of 2009
# Note that this is the day of the week of the input date
days = date(2009, 1, 1) + date.timedelta(days=days)

# Output the day of the week of the input date
print(days.strftime("%A"))
