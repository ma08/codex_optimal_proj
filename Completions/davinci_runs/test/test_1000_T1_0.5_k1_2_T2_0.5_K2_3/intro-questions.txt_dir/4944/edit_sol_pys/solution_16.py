
import sys

def main():
    n = int(sys.stdin.readline())
    printers = [1] # initially there is one printer
    days = 0
    while sum(printers) < n:
        days += 1
        new_printers = 0 # number of new printers
        while printers:
            if printers[-1] > 1:
                printers[-1] -= 1
                new_printers += 1
            else:
                printers.pop()
        printers.extend([1]*new_printers)
    print(days)

main()
