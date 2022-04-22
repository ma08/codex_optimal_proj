import os
import sys

# os.path.join(path1[, path2[, ...]])
# os.path.join('folder1', 'folder2', 'folder3', 'file.png')
# 'folder1\\folder2\\folder3\\file.png'

# os.path.exists(path)
# os.path.exists('c:\\Windows')
# True
# os.path.exists('c:\\some_made_up_folder')
# False

# os.path.isfile(path)
# os.path.isfile('c:\\Windows\\system.ini')
# True
# os.path.isfile('c:\\Windows')
# False

# os.path.isdir(path)
# os.path.isdir('c:\\Windows\\system.ini')
# False
# os.path.isdir('c:\\Windows')
# True

# os.path.abspath(path)
# os.path.abspath('.')
# 'C:\\Python34'
# os.path.abspath('..\\.\\Scripts')
# 'C:\\Python34\\Scripts'

# os.path.relpath(path, start)
# os.path.relpath('C:\\Windows', 'C:\\')
# 'Windows'
# os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
# '..\\..\\Windows'

# os.getcwd()
# os.getcwd()
# 'C:\\Python34'

# os.chdir(path)
# os.chdir('C:\\Windows\\System32')
# os.getcwd()
# 'C:\\Windows\\System32'

# os.makedirs(path)
# os.chdir('C:\\')
# os.makedirs('C:\\delicious\\walnut\\waffles')

# os.path.basename(path)
# os.path.basename('c:\\Users\\Al')
# 'Al'
# os.path.basename('c:\\Users\\Al\\bacon.txt')
# 'bacon.txt'

# os.path.dirname(path)
# os.path.dirname('c:\\Users\\Al\\bacon.txt')
# 'c:\\Users\\Al'
# os.path.dirname('c:\\Users\\Al')
# 'c:\\Users'

# os.path.split(path)
# os.path.split('c:\\Users\\Al\\bacon.txt')
# ('c:\\Users\\Al', 'bacon.txt')

# os.path.getsize(path)
# os.path.getsize('c:\\Windows\\System32\\calc.exe')
# 74752

# os.listdir(path)
# os.listdir('c:\\Windows\\System32')
# ['0409', '7B296FB0-376B-497e-B012-9C450E1B7327-5P-0.C7483456-A289-439d-8115-601632D005A0',
# '7B296FB0-376B-497e-B012-9C450E1B7327-5P-1.C7483456-A289-439d-8115-601632D005A0', 'aaclient.dll', ...]

# os.path.exists('c:\\delicious')
# True
# os.listdir('c:\\delicious')
# ['walnut']
# os.listdir('c:\\delicious\\walnut')
# ['waffles']

# totalSize = 0
# for filename in os.listdir('c:\\delicious'):
#     totalSize = totalSize + os.path.getsize(os.path.join('c:\\delicious', filename))
# print(totalSize)

# os.path.exists('c:\\delicious')
# True
# os.path.exists('c:\\delicious\\walnut')
# True
# os.path.exists('c:\\delicious\\walnut\\waffles')
# True
# os.path.exists('c:\\delicious\\walnut\\pancakes')
# False

# os.path.isfile('c:\\delicious')
# False
# os.path.isfile('c:\\delicious\\walnut')
# False
# os.path.isfile('c:\\delicious\\walnut\\waffles')
# False
# os.path.isfile('c:\\delicious\\walnut\\pancakes')
# False

# os.path.isdir('c:\\delicious')
# True
# os.path.isdir('c:\\delicious\\walnut')
# True
# os.path.isdir('c:\\delicious\\walnut\\waffles')
# True
# os.path.isdir('c:\\delicious\\walnut\\pancakes')
# False

# os.path.getsize('c:\\delicious')
# 4096
# os.path.getsize('c:\\delicious\\walnut')
# 4096
# os.path.getsize('c:\\delicious\\walnut\\waffles')
# 0
# os.path.getsize('c:\\delicious\\walnut\\pancakes')
# Traceback (most recent call last):
#   File "<pyshell#22>", line 1, in <module>
#     os.path.getsize('c:\\delicious\\walnut\\pancakes')
# FileNotFoundError: [WinError 3] The system cannot find the path specified: 'c:\\delicious\\walnut\\pancakes'

# os.path.exists('C:\\Windows')
# True
# os.path.isdir('C:\\Windows')
# True
# os.path.isfile('C:\\Windows')
# False

# os.path.exists('C:\\Windows\\notepad.exe')
# True
# os.path.isdir('C:\\Windows\\notepad.exe')
# False
# os.path.isfile('C:\\Windows\\notepad.exe')
# True

# os.path.abspath('.')
# 'C:\\Python34'
# os.path.abspath('.\\Scripts')
# 'C:\\Python34\\Scripts'
# os.path.isabs('.')
# False
# os.path.isabs(os.path.abspath('.'))
# True

# os.path.relpath('C:\\Windows', 'C:\\')
# 'Windows'
# os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
# '..\\..\\Windows'

# os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
# '..\\..\\Windows'

# os.getcwd()
# 'C:\\Python34'
# os.chdir('C:\\Windows\\System32')
# os.getcwd()
# 'C:\\Windows\\System32'

# os.path.abspath('.')
# 'C:\\Windows\\System32'
# os.path.abspath('.\\System32')
# 'C:\\Windows\\System32\\System32'
# os.path.abspath('.\\..')
# 'C:\\Windows'
# os.path.abspath('.\\..\\..')
# 'C:\\'
# os.path.abspath('.\\..\\..\\..')
# 'C:\\'

# os.path.abspath
