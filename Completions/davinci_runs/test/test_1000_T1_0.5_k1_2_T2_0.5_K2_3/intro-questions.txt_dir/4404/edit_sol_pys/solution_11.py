
from datetime import datetime

s = input()

if datetime.strptime(s, '%Y/%m/%d') <= datetime(2019, 4, 30): #datetime.datetime.strptime(s, '%Y/%m/%d') <= datetime.datetime(2019, 4, 30):
    print('Heisei')
else:
    print('TBD')
