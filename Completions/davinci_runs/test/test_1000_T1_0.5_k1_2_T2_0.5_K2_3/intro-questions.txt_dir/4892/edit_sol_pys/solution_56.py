#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import argparse
import logging

# Set logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def parse_arguments():
    parser = argparse.ArgumentParser(description='file')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
    parser.add_argument('-i', '--input', type=str, default='file.in', help='input file')
    parser.add_argument('-o', '--output', type=str, default='file.out', help='output file')
    parser.add_argument('-s', '--solution', type=str, default=None, help='solution to compare')
    return parser.parse_args()
import sys

def read_input(inp):
    N = int(inp.readline())
    pwds = []
    for i in range(N):
        pwds.append(inp.readline().split())
    return N, pwds

def solve(N, pwds):
    pwds.sort(key=lambda x: x[1])
    ans = 1
    for i in range(N):
        ans += (1 - float(pwds[i][1])) * (i + 1)
    return ans

def main():
    args = parse_arguments()
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    logger.debug('args: %s' % args)
    inp = open(args.input, 'r')
    N, pwds = read_input(inp)
    inp.close()
    ans = solve(N, pwds)
    print(ans)

if __name__ == '__main__':
    main()
