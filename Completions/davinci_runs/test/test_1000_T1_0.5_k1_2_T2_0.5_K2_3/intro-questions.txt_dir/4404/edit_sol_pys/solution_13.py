import sys


with open(sys.argv[1]) as f:
    for line in f:
        l = line.strip()
        print(l)

if datetime.strptime(s, '%Y/%m/%d') <= datetime(2019, 4, 30):
    print('Heisei')
else:
    print('TBD')
