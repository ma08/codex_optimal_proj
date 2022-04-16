

import sys
import math
import string
import itertools
import collections
import re

def main():
    P, N = map(int, sys.stdin.readline().split())
    parts = {}
    i = 1
    for line in sys.stdin:
        line = line.strip()
        if line in parts:
            parts[line] = min(parts[line], i)
        else:
            parts[line] = i
        i += 1
    if len(parts) == P:
        print(max(parts.values(), key=int))
    else:
        print("paradox avoided")

main()
