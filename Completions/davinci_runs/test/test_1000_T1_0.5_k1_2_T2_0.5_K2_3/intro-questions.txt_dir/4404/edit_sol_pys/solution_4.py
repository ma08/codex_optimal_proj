import datetime


s = input()

if datetime.datetime.strptime(s, '%Y/%m/%d') <= datetime.datetime(2019, 4, 30):
    print('Heisei')
else:
    print('TBD')
