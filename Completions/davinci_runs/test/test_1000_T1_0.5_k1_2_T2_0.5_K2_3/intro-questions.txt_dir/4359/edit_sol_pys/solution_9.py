#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from datetime import datetime
from subprocess import Popen, PIPE

# 脚本所在目录
SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0]

# 配置文件目录
CONFIG_PATH = os.path.join(SCRIPT_PATH, 'conf')

# 配置文件名
CONFIG_FILE = os.path.join(CONFIG_PATH, 'config.ini')

# 开始时间
start_time = datetime.now()

# 日志文件
LOG_FILE = os.path.join(SCRIPT_PATH, 'log', '%s.log' % start_time.strftime('%Y%m%d%H%M'))

# 日志文件
LOG_HANDLE = open(LOG_FILE, 'w')

# 读取配置文件
CONFIG = {}
with open(CONFIG_FILE, 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, value = line.split('=')
        CONFIG[key.strip()] = value.strip()


def log(content):
    LOG_HANDLE.write('%s %s\n' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), content))
    LOG_HANDLE.flush()


def get_file_list(path):
    file_list = []
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        if not os.path.isfile(file_path):
            continue
        file_list.append(file_path)
    return file_list


def get_size(f):
    size = os.path.getsize(f)
    return size


def get_file_type(f):
    cmd = 'file %s' % f
    p = Popen(cmd, shell=True, stdout=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return None
    file_type = stdout.split(':')[1].strip().lower()
    return file_type


def get_md5(f):
    cmd = 'md5sum %s' % f
    p = Popen(cmd, shell=True, stdout=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return None
    md5 = stdout.split()[0].strip()
    return md5


def get_sha1(f):
    cmd = 'sha1sum %s' % f
    p = Popen(cmd, shell=True, stdout=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return None
    sha1 = stdout.split()[0].strip()
    return sha1


def get_sha256(f):
    cmd = 'sha256sum %s' % f
    p = Popen(cmd, shell=True, stdout=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return None
    sha256 = stdout.split()[0].strip()
    return sha256


def get_ssdeep(f):
    cmd = 'ssdeep %s' % f
    p = Popen(cmd, shell=True, stdout=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return None
    ssdeep = stdout.split()[1].strip()
    return ssdeep


def main():
    log('start')
    log('config file: %s' % CONFIG_FILE)
    log('log file: %s' % LOG_FILE)
    log('start time: %s' % start_time)
    log('=' * 40)

    scan_path = CONFIG.get('scan_path')
    if not scan_path:
        log('scan_path not config, exit')
        sys.exit(1)

    log('scan_path: %s' % scan_path)

    if not os.path.exists(scan_path):
        log('scan_path not exists, exit')
        sys.exit(1)

    log('=' * 40)

    file_list = get_file_list(scan_path)
    log('file count: %s' % len(file_list))

    log('=' * 40)

    for f in file_list:
        log(f)

    log('=' * 40)

    log('end')


if __name__ == '__main__':
    main()
