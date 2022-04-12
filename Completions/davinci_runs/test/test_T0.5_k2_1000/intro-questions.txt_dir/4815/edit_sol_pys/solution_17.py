#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import stat

# 列出目录
print(os.listdir('.'))

# 判断是否是文件
print(os.path.isfile('file.py'))

# 判断是否是目录
print(os.path.isdir('file.py'))

# 判断是否是绝对路径
print(os.path.isabs('file.py'))

# 获取文件名
print(os.path.basename('file.py'))

# 获取文件所在目录
print(os.path.dirname('file.py'))

# 获取文件大小
print(os.path.getsize('file.py'))

# 获取文件绝对路径
print(os.path.abspath('file.py'))

# 获取文件绝对路径，并分割成目录与文件名
print(os.path.split(os.path.abspath('file.py')))

# 分割路径，返回路径各部分的元组
print(os.path.splitdrive(os.path.abspath('file.py')))

# 分割文件名与扩展名，返回(fname, fextension)元组
print(os.path.splitext(os.path.abspath('file.py')))

# 获取路径分隔符
print(os.path.sep)

# 获取当前目录
print(os.getcwd())

# 切换当前目录
os.chdir('/Users/michael/testdir')

# 创建目录
os.mkdir('testdir')

# 删除目录
os.rmdir('testdir')

# 删除文件
os.remove('test.txt')

# 创建多级目录
os.makedirs('testdir/testdir2')

# 删除多级目录
os.removedirs('testdir/testdir2')

# 改变文件权限与时间戳
os.chmod('test.py', stat.S_IRWXU)
os.utime('test.py', (1525746400, 1525746400))

# 重命名文件
os.rename('test.txt', 'test.py')

# 获取文件属性
print(os.stat('test.py'))

# 获取文件属性
print(os.stat('test.py').st_size)

# 获取文件属性
print(os.stat('test.py').st_mtime)

# 获取文件属性
print(os.stat('test.py').st_atime)

# 获取文件属性
print(os.stat('test.py').st_ctime)

# 获取文件属性
print(os.stat('test.py').st_mode)

# 获取文件属性
print(os.stat('test.py').st_ino)

# 获取文件属性
print(os.stat('test.py').st_dev)

# 获取文件属性
print(os.stat('test.py').st_nlink)

# 获取文件属性
print(os.stat('test.py').st_uid)

# 获取文件属性
print(os.stat('test.py').st_gid)

# 获取文件属性
print(os.stat('test.py').st_size)

# 获取文件属性
print(os.stat('test.py').st_atime)

# 获取文件属性
print(os.stat('test.py').st_mtime)

# 获取文件属性
print(os.stat('test.py').st_ctime)

# 获取文件属性
print(os.stat('test.py').st_blksize)

# 获取文件属性
print(os.stat('test.py').st_blocks)

# 列出当前目录下所有目录，结果以列表形式打印
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出当前目录下所有.py文件，结果以列表形式打印
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
