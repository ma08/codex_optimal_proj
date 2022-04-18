

import sys
import math
import string
import itertools
import collections
import re

def main():
    P, N = [int(i) for i in sys.stdin.readline().split()]
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
        print(max(parts.values()))
    else:
        print("paradox avoided")

main()