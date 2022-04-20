#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

def file_info(f):
    try:
        stat = os.stat(f)
        return stat
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_list(d):
    try:
        return os.listdir(d)
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_stat(f):
    try:
        stat = os.stat(f)
        mode = stat.st_mode
        return mode
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_type(f):
    try:
        mode = os.stat(f).st_mode
        if os.path.isfile(f):
            return "file"
        elif os.path.isdir(f):
            return "dir"
        elif os.path.islink(f):
            return "link"
        elif os.path.ismount(f):
            return "mount"
        elif mode & 0o170000 == 0o120000:
            return "socket"
        elif mode & 0o170000 == 0o140000:
            return "fifo"
        elif mode & 0o170000 == 0o100000:
            return "char_device"
        elif mode & 0o170000 == 0o200000:
            return "block_device"
        else:
            return "unknown"
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_size(f):
    try:
        stat = os.stat(f)
        return stat.st_size
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_mtime(f):
    try:
        stat = os.stat(f)
        return stat.st_mtime
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_ctime(f):
    try:
        stat = os.stat(f)
        return stat.st_ctime
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_atime(f):
    try:
        stat = os.stat(f)
        return stat.st_atime
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_owner(f):
    try:
        stat = os.stat(f)
        return stat.st_uid
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_group(f):
    try:
        stat = os.stat(f)
        return stat.st_gid
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_mode(f):
    try:
        stat = os.stat(f)
        return stat.st_mode
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_inode(f):
    try:
        stat = os.stat(f)
        return stat.st_ino
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_dev(f):
    try:
        stat = os.stat(f)
        return stat.st_dev
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_nlink(f):
    try:
        stat = os.stat(f)
        return stat.st_nlink
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_block_size(f):
    try:
        stat = os.stat(f)
        return stat.st_blksize
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_blocks(f):
    try:
        stat = os.stat(f)
        return stat.st_blocks
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_readable(f):
    try:
        mode = os.stat(f).st_mode
        if mode & 0o400 == 0o400:
            return True
        else:
            return False
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_writable(f):
    try:
        mode = os.stat(f).st_mode
        if mode & 0o200 == 0o200:
            return True
        else:
            return False
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_executable(f):
    try:
        mode = os.stat(f).st_mode
        if mode & 0o100 == 0o100:
            return True
        else:
            return False
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return None

def file_exists(f):
    try:
        os.stat(f)
        return True
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return False

def file_is_file(f):
    try:
        return os.path.isfile(f)
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return False

def file_is_dir(f):
    try:
        return os.path.isdir(f)
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return False

def file_is_link(f):
    try:
        return os.path.islink(f)
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return False

def file_is_mount(f):
    try:
        return os.path.ismount(f)
    except OSError, e:
        sys.stderr.write("%s\n" % e)
        return False
