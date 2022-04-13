#!/bin/python3
#inputs
from datetime import date

d, m = map(int, input().split()) #input is in this format: day, month
d = date(2009, m, d) #year is not relevant for this problem
print(d.strftime('%A')) #%A is the format for the full weekday name
