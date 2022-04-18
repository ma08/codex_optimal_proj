

from sys import stdin

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']

def get_day_of_week(day, month):
    day_of_year = sum(days_in_month[:month-1]) + day
    return day_of_week[(day_of_year + 4) % 7]

def main():
    day, month = [int(x) for x in stdin.readline().strip().split()]
    print(get_day_of_week(day, month))

if __name__ == '__main__':
    main()
