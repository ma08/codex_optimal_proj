
import datetime

d, m = [int(x) for x in input().split()]

days = datetime.date(2009, m, d) - datetime.date(2009, 1, 1) 

days = days.days % 7

days = datetime.date(2009, 1, 1) + datetime.timedelta(days=days)

print(days.strftime("%A"))
