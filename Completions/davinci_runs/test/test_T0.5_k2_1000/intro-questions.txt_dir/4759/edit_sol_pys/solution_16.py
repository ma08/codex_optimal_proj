import sys
import math

n = int(input())
at_bats = list(map(int, input().split()))  # at_bats is a list of ints

bases = 0
official_at_bats = 0  # official_at_bats is the number of at_bats that are not -1

for at_bat in at_bats:
    if at_bat == -1:  # if at_bat is -1, then it is not an official at_bat
        continue
    else:
        official_at_bats += 1  # add 1 to official_at_bats
        bases += at_bat  # add at_bat to bases

slugging_percentage = bases / official_at_bats  # slugging_percentage is the number of bases divided by the number of official_at_bats

print(slugging_percentage)
