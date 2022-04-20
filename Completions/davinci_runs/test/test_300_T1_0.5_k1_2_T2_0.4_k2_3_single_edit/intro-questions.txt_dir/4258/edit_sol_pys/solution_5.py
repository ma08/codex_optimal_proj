import os
import sys
import stat

def show_file_info(filename):
    stat_info = os.stat(filename)
    print('\tMode :', oct(stat_info.st_mode))
    print('\tCreated :', stat_info.st_ctime)
    print('\tAccessed:', stat_info.st_atime)
    print('\tModified:', stat_info.st_mtime)

filename = 'file.py'

print('File         :', filename)
print('Access time  :', os.stat(filename).st_atime)
print('Modified time:', os.stat(filename).st_mtime)

print('Setting access time to', os.stat(filename).st_mtime)
os.utime(filename, (os.stat(filename).st_atime, os.stat(filename).st_mtime))

print('Access time  :', os.stat(filename).st_atime)
print('Modified time:', os.stat(filename).st_mtime)

print('Changing mode of', filename, 'to rwxrwxrwx')
os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-xr-x')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP | stat.S_IWOTH)

print('Mode         :', oct(os.stat(filename).st_mode))

print('Changing mode of', filename, 'to r-xr-x-wx')
os.chmod(filename, stat.S_IXUSR | stat.S_IXGRP
