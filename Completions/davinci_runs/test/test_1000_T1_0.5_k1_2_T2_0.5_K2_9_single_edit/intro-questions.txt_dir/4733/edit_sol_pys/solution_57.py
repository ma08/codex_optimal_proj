

import sys
import math
def main():
    x = int(sys.stdin.readline().strip())
    if x % 2 == 0:
        print(x // 2)
    else:
        print((x + 1) // 2)
main()
