#!/usr/bin/env python3

import sys

def is_halloween(date):
    month, day = date.split()  # split date into month and day
    month = month.upper()  # convert month to uppercase
    day = int(day)  # convert day to int

    if month == "OCT" and day == 31:  # check for halloween
        return "yup"
    elif month == "DEC" and day == 25:  # check for christmas
        return "yup"
    else:  # otherwise, it's not halloween
        return "nope"

def main():
    date = sys.stdin.readline().strip()  # read in date from stdin
    print(is_halloween(date))  # print if it's halloween

if __name__ == "__main__":
    main()
