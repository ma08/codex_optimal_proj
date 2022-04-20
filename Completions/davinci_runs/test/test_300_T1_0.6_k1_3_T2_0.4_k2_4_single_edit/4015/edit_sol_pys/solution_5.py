#!/usr/bin/env python3

import sys
import os
import shutil

def main():
    print('Arguments: ', sys.argv)

    if len(sys.argv) < 3:
        print('Usage: python3 {} <source_dir> <destination_dir>'.format(sys.argv[0]))
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    if not os.path.exists(source):
        print('Source directory does not exist')
        sys.exit(1)

    if not os.path.exists(destination):
        print('Destination directory does not exist')
        sys.exit(1)

    for filename in os.listdir(source):
        if filename.endswith('.txt'):
            shutil.copy(os.path.join(source, filename), destination)

if __name__ == '__main__':
    main()
