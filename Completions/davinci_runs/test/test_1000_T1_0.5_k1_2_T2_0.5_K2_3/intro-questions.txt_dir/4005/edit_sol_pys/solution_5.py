#!/usr/bin/env python3

import os
import sys
import time
import random


def main():
    file_path = sys.argv[1:]
    if not os.path.isfile(file_path[0]):
        print('File path {} does not exist. Exiting...'.format(file_path[0]))
        sys.exit()

    with open(file_path[0]) as f:
        for line in f:
            print(line)
            time.sleep(random.randint(1,10))


if __name__ == '__main__':
    main()
