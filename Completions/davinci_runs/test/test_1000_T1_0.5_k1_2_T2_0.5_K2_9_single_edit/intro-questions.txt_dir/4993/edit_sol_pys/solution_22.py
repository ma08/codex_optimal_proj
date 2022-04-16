

import sys
import math
import string
import itertools
import collections
import re

def main():
    P, N = [int(i) for i in input().split()]
    parts = {}
    i = 1
    for part in sys.stdin:
        part = part.strip()
        if part in parts:
            parts[part] = min(parts[part], i)
        else:
            parts[part] = i
        i += 1
    if len(parts) == P:
        print(max(parts.values()))
    else:
        print("paradox avoided")

main()
