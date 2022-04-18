# Simon says

import sys

for _ in range(int(sys.stdin.readline())):
    print(sys.stdin.readline()) if sys.stdin.readline().startswith("Simon says") else 0
