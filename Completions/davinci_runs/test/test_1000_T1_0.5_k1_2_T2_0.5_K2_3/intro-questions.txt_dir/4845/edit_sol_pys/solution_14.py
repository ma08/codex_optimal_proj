# inputs
from datetime import date

d, m = map(int, input().split())
d = date(2009, m, d)
print(d.strftime('%A'))
