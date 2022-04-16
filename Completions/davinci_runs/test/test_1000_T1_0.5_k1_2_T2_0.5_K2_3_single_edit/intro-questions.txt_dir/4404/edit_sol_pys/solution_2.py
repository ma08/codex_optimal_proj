
from datetime import datetime

# input
s = input()

# convert
date = datetime.strptime(s, '%Y/%m/%d')

# process
if date <= datetime(2019, 5, 1):
    print('Heisei')
else:
    print('TBD')
