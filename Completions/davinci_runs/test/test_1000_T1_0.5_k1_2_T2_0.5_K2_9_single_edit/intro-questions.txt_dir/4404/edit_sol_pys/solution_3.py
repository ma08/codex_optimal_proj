

from datetime import datetime

s = input()

if datetime.strptime(s, '%Y/%m/%d') <= datetime(2019, 5, 1):
    print('Heisei')
else:
    print('TBD')
