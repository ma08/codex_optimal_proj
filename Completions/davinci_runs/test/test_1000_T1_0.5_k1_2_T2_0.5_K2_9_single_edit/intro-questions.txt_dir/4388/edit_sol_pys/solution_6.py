

import sys

n = int(input())

if (111 <= n <= 999):
    n = str(n)
    n = n.replace("1", "*")
    n = n.replace("9", "1")
    n = n.replace("*", "9")
    print(n)
else:
    sys.exit()
