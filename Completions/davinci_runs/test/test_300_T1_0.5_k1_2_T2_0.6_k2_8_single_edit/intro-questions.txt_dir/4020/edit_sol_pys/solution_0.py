

import math

h1, m1 = [int(x) for x in input().split(':')]
h2, m2 = [int(x) for x in input().split(':')]

m3 = int(math.ceil((m1 + m2) / 2))
h3 = (h1 + (m1 + m2) // 120) % 24

print('{:02}:{:02}'.format(h3, m3))
