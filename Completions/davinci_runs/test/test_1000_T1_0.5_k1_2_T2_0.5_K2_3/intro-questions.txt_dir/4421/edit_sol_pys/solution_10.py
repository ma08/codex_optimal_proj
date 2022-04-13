
n,k = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

d.sort()

# build a lookup table for each mode value
mods = [0] * k
for i in d:
    mods[i % k] += 1

# find the most common mode value
max_mod_val = 0
for i in range(k):
    if mods[i] > mods[max_mod_val]:
        max_mod_val = i

# find the number of pairs that can be made with the most common mode value
num_pairs = int(mods[max_mod_val] / 2)

# find the number of pairs that can be made with the second most common mod value
if k % 2 == 0:
    if max_mod_val == int(k / 2):
        num_pairs += int(mods[0] / 2)
    else:
        num_pairs += int(min(mods[max_mod_val], mods[k-max_mod_val])/2)

print(2*num_pairs)
