from sys import stdin

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
               'Saturday', 'Sunday']


def get_day_of_week(d, m):
    day_of_year = sum(days_in_month[:m - 1]) + d
    return day_of_week[(day_of_year + 3) % len(day_of_week)]

def main():
    d, m = [int(x) for x in stdin.readline().strip().split()]
    print(get_day_of_week(d, m))

if __name__ == '__main__':
    main()
