#!/usr/bin/python3

import json
import sys


def main():
    for line in sys.stdin:
        data = json.loads(line)
        if data['type'] == 'file':
            print(data['data']['name'])


if __name__ == '__main__':
    main()
