#!/usr/bin/env python3

import sys
import math

def parse_line(line):
    return [int(x) for x in line.split()]

def add(a, b, c, d):
    return a + b == c + d

def subtract(a, b, c, d):
    return a - b == c - d

def multiply(a, b, c, d):
    return a * b == c * d

# a + b = c + d
if a + b == c + d:
    valid.append('{} + {} = {} + {}'.format(a, b, c, d))

# a - b = c - d
if a - b == c - d:
    valid.append('{} - {} = {} - {}'.format(a, b, c, d))

# a * b = c * d
if a * b == c * d:
    valid.append('{} * {} = {} * {}'.format(a, b, c, d))

# a / b = c / d
if b != 0 and d != 0 and a / b == c / d:
    valid.append('{} / {} = {} / {}'.format(a, b, c, d))

if len(valid) > 0:
    print('\n'.join(sorted(valid)))
else:
    print('problems ahead')
