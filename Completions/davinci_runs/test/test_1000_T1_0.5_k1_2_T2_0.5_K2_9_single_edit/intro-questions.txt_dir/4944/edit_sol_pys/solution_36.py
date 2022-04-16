
from sys import stdin, stdout

n = int(stdin.readline().strip())

printers = 1
days = 1
while printers < n:
    printers += printers

stdout.write(str(days))
