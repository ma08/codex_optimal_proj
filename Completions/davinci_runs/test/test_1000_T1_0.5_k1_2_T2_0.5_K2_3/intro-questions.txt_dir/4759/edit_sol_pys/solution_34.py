#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline())
bases = list(map(int, sys.stdin.readline().split()))

# The number of official at-bats is the number of bases that are not walk
official_at_bats = len([base for base in bases if base != -1])

# The total number of bases is the sum of all bases
total_bases = sum(bases)

# The slugging percentage is total bases divided by official at-bats
slugging_percentage = total_bases / official_at_bats

print(slugging_percentage)
