

import sys

n = int(input())

n = str(n)
n = n.replace("1", "*")
n = n.replace("9", "1")
n = n.replace("*", "9")
print (n)
