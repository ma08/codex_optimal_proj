

# Program

n = int(input())

printers = 0
days = 0

while n > 0:
    days += 1
    printers += 1
    n -= printers

print(days)
