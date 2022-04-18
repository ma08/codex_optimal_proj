#!/usr/bin/env python3

import os
import sys
import time


def main():
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print('File path {} does not exist. Exiting...'.format(file_path))
        sys.exit()

    with open(file_path) as f:
        for line in f:
            print(line.strip())
            time.sleep(2)


if __name__ == '__main__':
    main()
