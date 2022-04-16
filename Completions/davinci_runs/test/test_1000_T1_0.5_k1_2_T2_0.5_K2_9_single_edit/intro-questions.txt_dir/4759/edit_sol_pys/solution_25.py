
import sys

n = int(sys.stdin.readline())
bases = list(map(int, sys.stdin.readline().split()))

official_at_bats = len([base for base in bases if base != -1])

total_bases = sum(bases)

slugging_percentage = total_bases / official_at_bats

print(slugging_percentage)
