

# -*- coding: utf-8 -*- 

# ------ Print the number of days in the month. ------

# Read an integer: 
month = int(input())
# Print a value: 
if month == 2:
    print('28')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('30')
else:
    print('31')
