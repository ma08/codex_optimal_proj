

from sys import stdin, argv

x = float(argv[1])

print(int(x*1000*5280/4854 + .5))
