#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import re
import sys


def main(argv):
    file_name = argv[1]
    if not os.path.isfile(file_name):
        print("File path {} does not exist. Exiting...".format(file_name))
        sys.exit()
    # reading data from file
    with open(file_name, 'r') as file:
        data = file.read().replace('\n', '')
    # parsing data
    data = re.sub(' +', ' ', data)
    data = data.split(' ')
    # print(data)
    # initializing variables
    index = 0
    current_time = time.time()
    previous_time = current_time
    # writing data to file
    while index < len(data):
        current_time = time.time()
        if current_time - previous_time > 0.01:
            with open(file_name, 'a') as file:
                file.write(data[index] + ' ')
            index += 1
            previous_time = current_time


if __name__ == "__main__":
    main(sys.argv)
