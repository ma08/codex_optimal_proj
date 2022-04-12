
from datetime import datetime

s = input('input date: ')

if datetime.strptime(s, '%Y/%m/%d') <= datetime(2019, 4, 30, 0, 0, 0):
    print('Heisei')
else:
    print('TBD')
