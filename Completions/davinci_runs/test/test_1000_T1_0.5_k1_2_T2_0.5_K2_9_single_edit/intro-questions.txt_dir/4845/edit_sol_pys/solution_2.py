#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main():
    d, m = map(int, sys.stdin.readline().split()) # read input
    days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0 # day of the week
    for i in range(m-1):
        day += months[i] 
    day += d
    print(days[day % 7]) # print the day of the week

if __name__ == '__main__':
    main()
