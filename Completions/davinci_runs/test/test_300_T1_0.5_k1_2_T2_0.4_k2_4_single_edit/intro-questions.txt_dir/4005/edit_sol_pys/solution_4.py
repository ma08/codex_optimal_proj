#!/usr/bin/env python

import sys
import os
import shutil

def main():
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " <source> <destination>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    if not os.path.exists(source):
        print("Source does not exist")
        sys.exit(1)

    if not os.path.isdir(destination):
        print("Destination is not a directory")
        sys.exit(1)

    if os.path.exists(destination + "/" + os.path.basename(source)):
        print("Destination already exists")
        sys.exit(1)

    shutil.copy(source, destination)
    print("Copied " + source + " to " + destination)

if __name__ == "__main__":
    main()
