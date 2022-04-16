

# This program will output the day of the week of the input date
# The algorithm used is as follows:
# 1. Determine the number of days between the start of 2009 and the input date
# 2. Find the day of the week of the start of 2009
# 3. Add the number of days to the start of 2009 and output the day of the week

# Import date time library
import datetime

# Get input
d, m = [int(x) for x in input().split()]

# Calculate the number of days between the start of 2009 and the input date
# Note that this is a negative number for dates before the start of 2009
days = datetime.date(2009, m, d) - datetime.date(2009, 1, 1)

# Find the day of the week of the start of 2009
# Note that this is the day of the week of the start of 2009
days = days.days % 7

# Add the number of days to the start of 2009
# Note that this is the day of the week of the input date
days = datetime.date(2009, 1, 1) + datetime.timedelta(days=days)

# Output the day of the week of the input date
print(days.strftime("%A"))
