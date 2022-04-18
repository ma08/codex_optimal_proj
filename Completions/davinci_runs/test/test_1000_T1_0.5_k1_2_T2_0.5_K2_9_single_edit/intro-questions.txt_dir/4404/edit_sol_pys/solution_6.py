
from datetime import datetime
s = datetime.strptime(input(), '%Y/%m/%d')
print('Heisei' if s <= datetime(2019, 4, 30) else 'TBD')
