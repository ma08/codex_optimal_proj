#!/usr/bin/python


import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ./file.py [filename]")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        for line in f:
            if line == "\n":
                continue
            print(line, end="")


class MarsLaunch():
    def __init__(self, year):
        self.year = year
        self.month = 0

    def is_launch_window(self):
        if self.month == 12:
            self.month = 0
            self.year += 1
        else:
            self.month += 1

        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            self.month_days = 31
        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            self.month_days = 30
        elif self.month == 2:
            if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
                self.month_days = 29
            else:
                self.month_days = 28

        if self.month_days == 30:
            return True
        else:
            return False

main()
