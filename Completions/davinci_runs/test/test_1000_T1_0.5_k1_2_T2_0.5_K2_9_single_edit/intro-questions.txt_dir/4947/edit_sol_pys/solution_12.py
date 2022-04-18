

from sys import stdin

for line in stdin:
    x = float(line)
    print(int(x*1000*5280/4854 + .5))
