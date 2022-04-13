

from datetime import datetime

# input
s = input()

# convert
date = datetime.strptime(s, '%Y/%m/%d')

# process
if date <= datetime(2019, 4, 30):
    print('Heisei')
else:
    print('TBD')
