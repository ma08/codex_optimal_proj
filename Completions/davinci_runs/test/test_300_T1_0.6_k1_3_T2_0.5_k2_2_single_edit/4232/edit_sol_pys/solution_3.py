#!/usr/bin/env python

import sys
import os
import re
import tempfile
import shutil
import subprocess

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='file to be fixed')
    parser.add_argument('--out', '-o', type=str, help='output file')
    parser.add_argument('--replace', '-r', action='store_true', default=False, help='replace the file')
    parser.add_argument('--no-backup', '-b', action='store_false', default=True, help='do not backup the file')
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print('file does not exist')
        return

    if args.replace and not args.out:
        args.out = args.file

    tempdir = tempfile.mkdtemp()
    tempfile = os.path.join(tempdir, os.path.basename(args.file))

    subprocess.call(['vim', '-c', 'set fileformat=unix', '-c', 'wq', args.file])
    subprocess.call(['vim', '-c', 'set fileformat=unix', '-c', 'wq', args.file])

    subprocess.call(['vim', '-c', 'set fileformat=unix', '-c', 'wq', args.file])
    subprocess.call(['vim', '-c', 'set fileformat=unix', '-c', 'wq', args.file])

    subprocess.call(['vim', '-c', 'set fileformat=unix', '-c', 'wq', args.file])
    subprocess.call(['vim', '-c', 'set fileformat=unix', '-c', 'wq', args.file])

    if args.replace:
        if args.no_backup:
            shutil.copy(args.file, args.file + '.bak')
        shutil.move(tempfile, args.out)
    else:
        print('new file: {}'.format(tempfile))

    shutil.rmtree(tempdir)


if __name__ == '__main__':
    main()
