import os
import time

source = ['/Users/swa/notes']
target_dir = '/Users/swa/backup'

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
