#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <file>" % sys.argv[0])
        sys.exit(1)

    file_name = sys.argv[1]
    if not os.path.exists(file_name):
        print("File %s does not exist" % file_name)
        sys.exit(1)

    file_size = os.path.getsize(file_name)
    print("File size: %d" % file_size)

    f = open(file_name, "rb")
    f.seek(0, os.SEEK_END)
    file_size = f.tell()
    print("File size: %d" % file_size)
    f.close()

    f = open(file_name, "rb")
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        print("Chunk size: %d" % len(chunk))
    f.close()

    f = open(file_name, "rb")
    for line in f:
        print("Line size: %d" % len(line))
    f.close()

if __name__ == "__main__":
    main()
