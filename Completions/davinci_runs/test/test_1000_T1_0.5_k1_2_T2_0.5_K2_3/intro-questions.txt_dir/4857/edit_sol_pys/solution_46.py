

import sys
import math

def main():
    l, w = map(int, sys.stdin.readline().rstrip().split())
    if w < 1 or w > 26 * l: # if the number of letters is less than 1 or more than 26 * l (number of letters of the string), it is impossible to make a string
        print("impossible")
        return
    s = ""
    for i in range(l): # make the string
        if w > 26:
            s += "z"
            w -= 26
        else:
            s += chr(w + 96)
            w = 0
    print(s)

if __name__ == "__main__":
    main()
