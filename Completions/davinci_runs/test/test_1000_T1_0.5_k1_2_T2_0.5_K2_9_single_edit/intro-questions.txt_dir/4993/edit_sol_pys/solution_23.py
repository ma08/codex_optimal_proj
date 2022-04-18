

import sys
import math
import string
import itertools
import collections
import re

def main():
    P = int(sys.stdin.readline().strip())
    parts = {}
    i = 0
    for line in sys.stdin:
        line = line.strip()
        if line in parts:
            parts[line] = min(parts[line], i+1)
        else:
            parts[line] = i+1
        i += 1
    if len(parts) == P:
        print(max(parts.values()))
    else:
        print("paradox avoided")

main()
