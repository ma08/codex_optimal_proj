
from sys import stdin, stdout

n = int(stdin.readline().strip())

printers = 1
days = 0
while printers < n:
    days += 1
    printers += printers

stdout.write(str(days + 1))
