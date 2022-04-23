import os
import time

source = ['"C:\\My Documents"', 'C:\\Code'] # Путь к директории или файлу, который нужно скопировать
target_dir = 'E:\\Backup' # Путь к директории, куда будет создана резервная копия

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip' # Имя архива с датой и временем создания

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source)) # Создание архива

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
