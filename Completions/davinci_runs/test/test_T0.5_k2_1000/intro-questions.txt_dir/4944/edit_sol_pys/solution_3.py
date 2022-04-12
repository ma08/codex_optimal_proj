
import sys

def main():
    n = int(sys.stdin.readline())
    printers = [1] # list of printers, each with a number of pages to print
    days = 0
    while sum(printers) < n: # while we haven't printed enough pages
        days += 1
        new_printers = 0 # number of new printers to add
        while printers:
            if printers[-1] > 1: # if the printer has more than one page to print
                printers[-1] -= 1
                new_printers += 1
            else:
                printers.pop()
        printers.extend([1]*new_printers)
    print(days)

main()
