import os
import time

source = ['"C:\\My Documents"', 'C:\\Code']  # 要备份的文件目录
target_dir = 'E:\\Backup'  # 备份文件存储目录

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'  # 备份文件名

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))  # 备份命令

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
