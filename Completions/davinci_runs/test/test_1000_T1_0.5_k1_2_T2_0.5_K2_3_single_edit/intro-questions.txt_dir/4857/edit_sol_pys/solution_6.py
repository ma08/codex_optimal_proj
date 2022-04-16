

import sys
import math

def main():
    l, w = map(int, sys.stdin.readline().rstrip().split())
    if w < 1 or w > 26 * l or w % l != 0:
        print("impossible")
        return
    s = ""
    for i in range(l):
        if w > 26 * l:
            s += "z"
            w -= 26 * l
        else:
            s += chr((w // l) + 96)
            w = 0
    print(s)

if __name__ == "__main__":
    main()
