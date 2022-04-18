
import math
import sys

froshes = int(sys.stdin.readline().strip())
combos = {}
for i in range(froshes):
    combo = sorted(list(map(int, sys.stdin.readline().strip().split())))
    if combo not in combos:
        combos[combo] = 1
    else:
        combos[combo] += 1

froshes_left = froshes
max_popularity = 0
for combo in combos:
    popularity = combos[combo]
    if popularity > max_popularity:
        max_popularity = popularity
    froshes_left -= popularity

if froshes_left < max_popularity:
    max_popularity = froshes_left

print(math.ceil(max_popularity/2))
