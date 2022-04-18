
#
import sys
import math

n = int(input())
at_bats = list(map(int, input().split()))  # list of the values of the at bats

bases = 0  # sum of the bases
official_at_bats = 0  # number of official at bats

for at_bat in at_bats:  # for each at bat
    if at_bat == -1:  # if it was a strikeout
        continue
    else:
        official_at_bats += 1  # add 1 to the number of official at bats
        bases += at_bat  # add the number of bases to the sum of the bases

slugging_percentage = bases / official_at_bats  # calculate the slugging percentage

print(slugging_percentage)
