#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import shutil
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='path to the file')
    parser.add_argument('-n', '--name', help='name of the file')
    parser.add_argument('-t', '--type', help='type of the file')
    parser.add_argument('-d', '--date', help='date of the file')
    return parser.parse_args()


def get_file_info(path):
    file_info = {}
    file_info['path'] = path
    file_info['name'] = os.path.basename(path)
    file_info['type'] = os.path.splitext(path)[1]
    file_info['date'] = time.strftime('%Y%m%d', time.localtime(os.path.getmtime(path)))
    return file_info


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def move_file(src, dst):
    if not os.path.exists(src):
        print('{} does not exist'.format(src))
        return
    if not os.path.exists(dst):
        print('{} does not exist'.format(dst))
        return
    shutil.move(src, dst)
    print('{} moved to {}'.format(src, dst))


def main():
    args = parse_args()
    file_info = get_file_info(args.path)
    if args.name:
        file_info['name'] = args.name
    if args.type:
        file_info['type'] = args.type
    if args.date:
        file_info['date'] = args.date
    dst_dir = os.path.join(os.path.dirname(file_info['path']), file_info['date'])
    dst_path = os.path.join(dst_dir, file_info['name'])
    create_dir(dst_dir)
    move_file(file_info['path'], dst_path)


if __name__ == '__main__':
    main()
