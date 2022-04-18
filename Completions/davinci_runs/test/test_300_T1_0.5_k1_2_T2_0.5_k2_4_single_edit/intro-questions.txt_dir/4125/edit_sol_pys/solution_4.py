

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:50:34
import os

import argparse
import logging
import json

from typing import Dict, List, Any

logger = logging.getLogger(__name__)

import sys

def solve(x, xs):
    xs = sorted(xs)
    x_min = xs[0]
    x_max = xs[-1]
    if x < x_min:
        x_max = x_max + (x_min - x)
    elif x > x_max:
        x_min = x_min - (x - x_max)
    return x_max - x_min


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default=sys.stdin, type=argparse.FileType('r'),
                        help='input file to process (default: stdin)')
    parser.add_argument('--output', default=sys.stdout, type=argparse.FileType('w'),
                        help='output file to write (default: stdout)')
    parser.add_argument('--log', default='INFO', type=str,
                        help='logging level (default: INFO)')
    args = parser.parse_args()

    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.log)
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                        level=numeric_level)

    n, x = map(int, args.input.readline().split())
    xs = list(map(int, args.input.readline().split()))
    args.output.write(str(solve(x, xs)))


if __name__ == '__main__':
    main()
