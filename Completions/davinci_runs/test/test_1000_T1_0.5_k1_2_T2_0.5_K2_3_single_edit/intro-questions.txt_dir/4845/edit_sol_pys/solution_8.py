
from datetime import datetime
from sys import stdin

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def main():
    day, month = [int(x) for x in stdin.readline().strip().split()]
    date = datetime(2009, month, day)
    print(day_of_week[date.weekday()])

if __name__ == '__main__':
    main()
