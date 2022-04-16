
from datetime import date

d, m = map(int, input().split()) # split date and month
d = date(2009, m, d) # create date using date class
print(d.strftime('%A')) # convert date to weekday
