
from datetime import datetime

# input, convert and process
print('Heisei' if datetime.strptime(input(), '%Y/%m/%d') <= datetime(2019, 4, 30) else 'TBD')
