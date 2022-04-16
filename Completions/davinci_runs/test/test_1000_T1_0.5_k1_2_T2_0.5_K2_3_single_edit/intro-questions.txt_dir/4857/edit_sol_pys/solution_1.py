

import sys
import math

def main():
    l, w = map(int, sys.stdin.readline().rstrip().split())
    s = ""
    if w >= 1 and w <= 26 * l:
        for i in range(l):
            if w > 26:
                s += "z"
                w -= 26
            else:
                s += chr(w + 96)
                w = 0
    else:
        s = "impossible"
    print(s)

if __name__ == "__main__":
    main()
