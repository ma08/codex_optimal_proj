
from datetime import date

day, month = map(int, input().split())
day = date(2009, month, day)
print(day.strftime('%A'))
