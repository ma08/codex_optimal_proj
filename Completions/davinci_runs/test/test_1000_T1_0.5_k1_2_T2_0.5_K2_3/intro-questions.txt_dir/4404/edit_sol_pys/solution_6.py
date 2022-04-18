from datetime import datetime


# datetime(year, month, day)
s = input()

if datetime.strptime(s, '%Y/%m/%d') <= datetime(2019, 5, 1):
    print('Heisei')
else:
    print('TBD')
