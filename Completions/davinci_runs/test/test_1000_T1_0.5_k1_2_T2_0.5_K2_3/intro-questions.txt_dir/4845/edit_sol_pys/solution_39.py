
from sys import stdin

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days in months
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # days of week


def get_day_of_week(day, month):  # function to get the day of week
    day_of_year = sum(days_in_months[:month - 1]) + day
    return days_of_week[(day_of_year + 3) % 7]  # return the day of week


def main():
    day, month = [int(x) for x in stdin.readline().strip().split()]  # get the day and month
    print(get_day_of_week(day, month))  # print the day of week


if __name__ == '__main__':
    main()
