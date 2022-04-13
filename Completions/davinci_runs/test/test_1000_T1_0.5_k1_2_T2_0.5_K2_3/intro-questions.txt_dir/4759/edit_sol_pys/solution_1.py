

import sys
import math

n = int(input())
atbats = list(map(int, input().split()))

bases = 0
official_atbats = 0

for atbat in atbats:
    if atbat == -1:
        continue
    official_atbats += 1
    bases += atbat

slugging_percentage = bases / official_atbats

print(slugging_percentage)
