#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
import codecs
import locale

#读取文件
def readFile(fileName):
    file = codecs.open(fileName, 'r', 'utf-8')
    content = file.read()
    file.close()
    return content

#保存文件
def saveFile(fileName, content):
    file = codecs.open(fileName, 'w', 'utf-8')
    file.write(content)
    file.close()

#删除文件
def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)

#获取文件的大小
def getFileSize(fileName):
    if os.path.exists(fileName):
        return os.path.getsize(fileName)
    else:
        return 0

#获取文件的创建时间
def getFileCreateTime(fileName):
    if os.path.exists(fileName):
        return time.localtime(os.path.getctime(fileName))
    else:
        return 0

#获取文件的修改时间
def getFileModifyTime(fileName):
    if os.path.exists(fileName):
        return time.localtime(os.path.getmtime(fileName))
    else:
        return 0

#获取文件的访问时间
def getFileAccessTime(fileName):
    if os.path.exists(fileName):
        return time.localtime(os.path.getatime(fileName))
    else:
        return 0

#获取文件的所有者
def getFileOwner(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_uid
    else:
        return 0

#获取文件的所有者名字
def getFileOwnerName(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_uid
    else:
        return 0

#获取文件的所有者组
def getFileGroup(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_gid
    else:
        return 0

#获取文件的所有者组名字
def getFileGroupName(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_gid
    else:
        return 0

#获取文件的权限
def getFilePermission(fileName):
    if os.path.exists(fileName):
        return oct(os.stat(fileName).st_mode)[-3:]
    else:
        return 0

#获取文件的访问次数
def getFileAccessCount(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_atime
    else:
        return 0

#获取文件的修改次数
def getFileModifyCount(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_mtime
    else:
        return 0

#获取文件的状态改变次数
def getFileStatusChangeCount(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_ctime
    else:
        return 0

#获取文件的创建时间
def getFileCreateTime(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_ctime
    else:
        return 0

#获取文件的链接数
def getFileLinkCount(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_nlink
    else:
        return 0

#获取文件的设备编号
def getFileDeviceID(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_dev
    else:
        return 0

#获取文件的inode编号
def getFileInodeID(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_ino
    else:
        return 0

#获取文件的硬链接
def getFileHardLink(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_nlink
    else:
        return 0

#获取文件的状态
def getFileStatus(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName)
    else:
        return 0

#获取文件的类型
def getFileType(fileName):
    if os.path.exists(fileName):
        return os.stat(fileName).st_mode
    else:
        return 0

#判断文件是否可读
def isFileReadable(fileName):
    if os.path.exists(fileName):
        return os.access(fileName, os.R_OK)
    else:
        return 0

#判断文件是否可写
def isFileWritable(fileName):
    if os.path.exists(fileName):
        return os.access(fileName, os.W_OK)
    else:
        return 0

#判断文件是否可执行
def isFileExecutable(fileName):
    if os.path.exists(fileName):
        return os.access(fileName, os.X_OK)
    else:
        return 0

#判断文件是否存在
def isFileExist(fileName):
    return os.path.exists(fileName)

#判断文件是否是绝对路径
def isFileAbsolute(fileName):
    return os.path.isabs(fileName)

#判断文件是否是符号链接
def isFileSymlink(fileName):
    return os.path.islink(fileName)

#判断文件是否是目录
def isFileDirectory(fileName):
    return os.path.isdir(fileName)

#
