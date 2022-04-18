
import sys

def main():
    n = int(next(sys.stdin).strip())
    printers = [1]
    days = 0
    while sum(printers) <= n:
        days += 1
        new_printers = 0
        for i in range(len(printers)):
            if printers[i] > 1:
                printers[i] -= 1
                new_printers += printers[i]
                printers[i] = 1
        printers.extend([1]*new_printers)
    print(days)

main()
