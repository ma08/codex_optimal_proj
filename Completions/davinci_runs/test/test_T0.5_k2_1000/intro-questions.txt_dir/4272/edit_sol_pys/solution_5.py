#!/usr/bin/env python3

import sys, re

N = int(input())
S = input()

print(len(re.findall("ABC", S)))
