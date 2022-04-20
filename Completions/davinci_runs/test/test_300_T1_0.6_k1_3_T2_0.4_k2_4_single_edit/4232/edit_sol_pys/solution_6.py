#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        print("{} is not a file".format(filename))
        sys.exit(1)

    with open(filename, 'rb') as f:
        data = f.read()

    print("{} is a {} file".format(filename, filetype(data)))

def filetype(data):
    if data.startswith(b'\x1f\x8b\x08'):
        return 'gzip'
    elif data.startswith(b'\x42\x5a\x68'):
        return 'bzip2'
    elif data.startswith(b'\x50\x4b\x03\x04'):
        return 'zip'
    elif data.startswith(b'\x37\x7a\xbc\xaf\x27\x1c'):
        return '7z'
    elif data.startswith(b'\x52\x61\x72\x21\x1a\x07\x00'):
        return 'rar'
    elif data.startswith(b'\x78\x01'):
        return 'dmg'
    elif data.startswith(b'\x25\x50\x44\x46'):
        return 'pdf'
    elif data.startswith(b'\x49\x44\x33'):
        return 'mp3'
    elif data.startswith(b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34\x32'):
        return 'mp4'
    elif data.startswith(b'\x00\x00\x00\x20\x66\x74\x79\x70\x69\x73\x6f\x6d'):
        return 'm4a'
    elif data.startswith(b'\x00\x00\x00\x20\x66\x74\x79\x70\x4d\x34\x41\x20'):
        return 'm4v'
    elif data.startswith(b'\x00\x00\x00\x1c\x66\x74\x79\x70\x4d\x34\x41\x20'):
        return 'm4v'
    elif data.startswith(b'\x00\x00\x00\x1c\x66\x74\x79\x70\x6d\x70\x34\x32'):
        return 'mp4'
    elif data.startswith(b'\x00\x00\x00\x1c\x66\x74\x79\x70\x4d\x53\x4e\x56'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x14\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x6d\x70\x34\x32'):
        return 'mp4'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x69\x73\x6f\x6d'):
        return 'm4a'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x4d\x34\x56\x20'):
        return 'm4v'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x4d\x34\x41\x20'):
        return 'm4v'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x4d\x53\x4e\x56'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x6d\x70\x34\x32'):
        return 'mp4'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x6d\x6d\x76\x68'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    elif data.startswith(b'\x00\x00\x00\x00\x66\x74\x79\x70\x71\x74\x20\x20'):
        return 'mov'
    else:
        return 'unknown'

if __name__ == '__main__':
    main()
