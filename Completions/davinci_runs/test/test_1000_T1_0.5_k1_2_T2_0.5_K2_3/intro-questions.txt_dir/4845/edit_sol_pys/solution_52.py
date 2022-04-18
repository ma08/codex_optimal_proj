
d, m = map(int, input().split())

days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
day = sum(days[:m]) + d
day %= 7

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(days_of_the_week[day])
