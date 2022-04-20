

a = int(input())
b = int(input())
c = int(input())
x = int(input())

import itertools
l = itertools.combinations_with_replacement([a,b,c], 3)
print(l)
