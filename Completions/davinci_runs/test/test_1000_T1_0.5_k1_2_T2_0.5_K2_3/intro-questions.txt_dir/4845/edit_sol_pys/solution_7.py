
d, m = map(int, input().split()) # input day and month

days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) # number of days in each month
day = sum(days[:m]) + d # sum of days before the month and the day
day %= 7

days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') # days of the week
print(days_of_week[day])
