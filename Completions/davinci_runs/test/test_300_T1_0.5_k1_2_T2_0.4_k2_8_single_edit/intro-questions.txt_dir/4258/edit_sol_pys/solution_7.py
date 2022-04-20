import os

os.chdir('/Users/david/Desktop')

print(os.getcwd())

print(os.listdir())

os.mkdir('new_dir')

os.makedirs('new_dir2/new_dir3')

os.rename('new_dir2/new_dir3', 'new_dir2/new_dir4')

os.rmdir('new_dir')

os.removedirs('new_dir2/new_dir4')

os.stat('file.py')

os.stat('file.py').st_size

os.stat('file.py').st_mtime

from datetime import datetime

mod_time = os.stat('file.py').st_mtime

print(datetime.fromtimestamp(mod_time))

os.chdir('/Users/david/Desktop')

for dirpath, dirnames, filenames in os.walk('/Users/david/Desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

print(file_path)

os.path.basename('/tmp/test.txt')

os.path.dirname('/tmp/test.txt')

os.path.split('/tmp/test.txt')

os.path.exists('/tmp/test.txt')

os.path.isdir('/tmp/test.txt')

os.path.isfile('/tmp/test.txt')

os.path.splitext('/tmp/test.txt')

dir(os.path)
