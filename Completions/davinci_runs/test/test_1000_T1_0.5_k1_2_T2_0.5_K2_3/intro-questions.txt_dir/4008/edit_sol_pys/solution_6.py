#!/usr/bin/env python

from __future__ import print_function

import argparse
import sys

from file_type import FileType
from file_type import FileTypeException


def parse_args(args):
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Identify file types')
    parser.add_argument('file', type=argparse.FileType('rb'),
                        help='file to identify')
    return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parsed_args = parse_args(args)

    file_type = FileType(parsed_args.file)
    try:
        print(file_type.get_type())
    except FileTypeException as e:
        print(e.message, file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
