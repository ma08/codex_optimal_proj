
n = int(input())
bases = [int(x) for x in input().split()]

valid_at_bats = 0
for base in bases:
    if base != -1:
        valid_at_bats += 1

total_bases = 0
for base in bases:
    if base != -1:
        total_bases += base

print(total_bases / valid_at_bats)
