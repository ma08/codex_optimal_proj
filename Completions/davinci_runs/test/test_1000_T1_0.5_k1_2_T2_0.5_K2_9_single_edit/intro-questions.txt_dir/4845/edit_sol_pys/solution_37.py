

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    total = meal_cost + tip + tax

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
