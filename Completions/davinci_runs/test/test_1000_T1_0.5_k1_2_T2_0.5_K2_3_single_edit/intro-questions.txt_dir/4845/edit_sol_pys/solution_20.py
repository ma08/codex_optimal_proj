

import datetime

d = int(input())
m = int(input())
y = int(input())

print(datetime.datetime(y, m, d).strftime('%A'))
