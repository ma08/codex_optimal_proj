

# Programm

n = int(input())

printers = 0
days = 0

while True:
    days += 1
    printers += 1
    n -= printers
    if n <= 0:
        print(days)
        break
