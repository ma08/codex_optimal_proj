
#1.py
import sys

def main():
    m = int(sys.stdin.readline())
    x = 1
    while x <= m:
        if len(set([a**3 + b**3 for a in range(1, x) for b in range(1, x)])) == x:
            print(x)
            break
        x += 1
    return 'none'

print(main())
