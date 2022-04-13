

n = int(input())
bases = [int(x) for x in input().split()]

# Calculate the number of valid at bats.
valid_at_bats = 0.0
for base in bases:
    if base != -1:
        valid_at_bats += 1

# Calculate the total bases.
total_bases = 0
for base in bases:
    if base != -1:
        total_bases += base

# Calculate and print the slugging percentage
print(float(total_bases) / float(valid_at_bats))
