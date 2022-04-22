#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
import sys, os

def read_input(filename):
    with open(filename, 'r') as f:
        return f.read().rstrip()

def write_output(filename, data):
    with open(filename, 'w') as f:
        f.write(str(data))

if can_eq(s, t):
    print('Yes')
else:
    print('No')
