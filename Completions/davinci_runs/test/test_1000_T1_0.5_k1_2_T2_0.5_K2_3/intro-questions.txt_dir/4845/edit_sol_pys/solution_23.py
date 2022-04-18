
from datetime import date

d, m = map(int, input().split())
d = date(2009, m, d).weekday()
print(d.strftime('%A'))
