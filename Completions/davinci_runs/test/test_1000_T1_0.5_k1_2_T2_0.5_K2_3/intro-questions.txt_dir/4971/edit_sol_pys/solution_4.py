

import sys

def main():
    m = int(sys.stdin.readline().strip())
    if m == 1:
        return 1
    for x in range(2, m + 1):
        if len(set([a**3 + b**3 for a in range(1, x) for b in range(1, x)])) == x - 1:
            return x - 1
    return 'None' 

print(main())
