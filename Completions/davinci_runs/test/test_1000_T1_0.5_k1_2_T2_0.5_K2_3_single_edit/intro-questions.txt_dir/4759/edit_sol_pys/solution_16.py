
import sys


def slugging_percentage(at_bats):
    bases = 0
    official_at_bats = 0

    for at_bat in at_bats:
        if at_bat == -1:
            continue
        else:
            official_at_bats += 1
            bases += at_bat

    return bases / official_at_bats

import math

n = int(input())
at_bats = list(map(int, input().split()))

bases = 0
official_at_bats = 0

for at_bat in at_bats:
    if at_bat == -1:
        continue
    else:
        official_at_bats += 1
        bases += at_bat

slugging_percentage = bases / official_at_bats

print(slugging_percentage)
