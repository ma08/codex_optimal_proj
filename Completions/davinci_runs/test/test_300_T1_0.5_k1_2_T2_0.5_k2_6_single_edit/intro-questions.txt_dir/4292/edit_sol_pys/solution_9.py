#!/usr/bin/env python3

import sys

n, k = map(int, sys.stdin.readline().split())  # Get the number of elements and the number of groups
p = list(map(int, sys.stdin.readline().split()))  # Get the elements

print(sum(sorted(p)[:k]))  # Print the sum of the smallest k elements
