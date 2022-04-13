
import sys

def main():
    n = int(next(sys.stdin))
    printers = [1] # list of number of printers per day
    days = 0
    while sum(printers) < n: # when the number of printers is less than n
        days += 1
        new_printers = 0 # number of new printers
        # check the printers on the last day
        for i in range(len(printers)):
            if printers[i] > 1: # if the last printer has more than 1
                printers[i] -= 1
                new_printers += 1 # add a new printer
            else:
                printers.pop() # if the last printer has 1, remove it
        printers.extend([1]*new_printers) # add new printers to the list
    print(days)

main()
