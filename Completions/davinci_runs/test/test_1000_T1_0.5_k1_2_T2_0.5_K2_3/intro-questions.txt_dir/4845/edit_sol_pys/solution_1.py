
from sys import stdin

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_day_of_week(day, month):
    day_of_year = sum(days_in_months[:month - 1]) + day
    return days_of_week[(day_of_year + 3) % 7]

def main():
    day, month = [int(x) for x in stdin.readline().strip().split()]
    print(get_day_of_week(day, month))

if __name__ == '__main__':
    main()
