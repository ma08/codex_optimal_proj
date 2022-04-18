

from sys import stdin

c11, c12, c13 = stdin.readline().rstrip().split() # a, b, c
c21, c22, c23 = stdin.readline().rstrip().split() # d, e, f
c31, c32, c33 = stdin.readline().rstrip().split() # g, h, i

print(c11 + c22 + c33)
