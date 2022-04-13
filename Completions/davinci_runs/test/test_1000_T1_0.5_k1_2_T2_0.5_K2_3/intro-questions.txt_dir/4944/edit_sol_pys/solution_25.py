
from sys import stdin

n = int(stdin.readline().strip())

printers = 1
days = 0
while printers < n:
    days += 1
    printers += printers

print(days + 1)
