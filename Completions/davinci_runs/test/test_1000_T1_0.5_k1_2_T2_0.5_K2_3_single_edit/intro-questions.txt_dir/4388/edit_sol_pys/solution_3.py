

import sys

n = int(input())

if (111 <= n <= 999):
    print (n.replace("1", "*").replace("9", "1").replace("*", "9"))
else:
    sys.exit()
