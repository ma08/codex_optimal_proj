#!/usr/bin/env python3

import os
import sys
import time


def main():
    file_paths = sys.argv[1:]
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print('File path {} does not exist. Exiting...'.format(file_path))
            sys.exit()

    for file_path in file_paths:
        with open(file_path) as f:
            for line in f:
                print(line)
                time.sleep(2)

        print('-' * 20)
        time.sleep(2)

    if len(file_paths) > 1:
        sys.exit()


if __name__ == '__main__':
    main()
