#!/usr/bin/env python3
# coding: utf-8


import sys, os, re

def read_stdin():
    return sys.stdin.read().rstrip()

S = read_stdin()
print(S.count("ABC"), S.count("ARC"))
