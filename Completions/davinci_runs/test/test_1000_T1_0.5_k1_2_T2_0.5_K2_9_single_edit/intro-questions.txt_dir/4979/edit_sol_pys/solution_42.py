

import sys

num = int(sys.stdin.readline().strip())
print(int(str(bin(num))[:1:-1], 2))
