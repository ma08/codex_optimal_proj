
n,k = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
d.sort()

mods = [0] * k
for i in d:
    mods[i%k] += 1


max_mod_val = 0
for i in range(k):
    if mods[i] > mods[max_mod_val]:
        max_mod_val = i


num_pairs = int(mods[max_mod_val]/2)


if k%2 == 0:
    if max_mod_val == int(k/2):
        num_pairs += int(mods[0]/2)
    else:
        num_pairs += int(min(mods[max_mod_val], mods[k-max_mod_val])/2)

print(2*num_pairs)
