
from datetime import datetime

# 入力
s = input()

# 変換
date = datetime.strptime(s, '%Y/%m/%d')

# process
if date <= datetime(2019, 4, 30):
    print('Heisei')
else:
    print('TBD')
