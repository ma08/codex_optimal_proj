
from sys import stdin, stdout

n = int(stdin.readline().strip())

pages = 1
days = 0
while pages < n:
    days += 1
    pages += pages

stdout.write(str(days + 1))
