

from itertools import permutations

a = input().split()
for i in permutations(a[0], int(a[1])):
    print(''.join(i))
