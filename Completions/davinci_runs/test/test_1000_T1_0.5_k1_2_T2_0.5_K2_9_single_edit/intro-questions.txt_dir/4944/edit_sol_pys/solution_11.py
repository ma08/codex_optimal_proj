

from sys import stdin, stdout

n = int(stdin.readline().strip())

printers = 0
days = 0
while printers <= n:
    if printers == 0:
        printers = 1
    days += 1
    printers += printers

stdout.write(str(days + 1))
