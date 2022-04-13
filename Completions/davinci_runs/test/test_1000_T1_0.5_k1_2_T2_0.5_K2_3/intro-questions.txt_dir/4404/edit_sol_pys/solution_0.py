

from datetime import datetime

# input date
s = input()

# convert date
date = datetime.strptime(s, '%Y/%m/%d')

# process date
if date <= datetime(2019, 5, 1):
    print('Heisei')
else:
    print('TBD')
