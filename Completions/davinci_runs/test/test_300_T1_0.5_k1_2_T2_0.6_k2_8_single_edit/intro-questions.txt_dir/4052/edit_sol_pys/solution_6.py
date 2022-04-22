from __future__ import print_function

import os
import json


def main():
    # set file path
    file_path = os.path.join(os.path.dirname(__file__), 'entries.txt')
    entries = []

    # read file
    with open(file_path, 'r') as f:
        for line in f:
            entry = json.loads(line)
            entries.append(entry)

    # loop through entries
    for entry in entries:
        print(entry['title'])


if __name__ == '__main__':
    main()
