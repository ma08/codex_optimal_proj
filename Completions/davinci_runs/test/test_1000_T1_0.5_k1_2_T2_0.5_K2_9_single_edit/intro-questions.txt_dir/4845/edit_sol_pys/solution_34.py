

from datetime import date

d, m = map(int, input().split())  # map function returns a list of results after applying the given function to each item of a given iterable
d = date(2009, m, d)
print(d.strftime('%A'))
