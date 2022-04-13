
import sys
import math

def main():
    l, w = map(int, sys.stdin.readline().rstrip().split())
    if w < 1 or w > 26 * l or l > 10 ** 9 or w > 10 ** 9:
        print("impossible")
        return
    s = ""
    for i in range(l):
        if w > 26:
            s += "z"
            w -= 26
        else:
            s += chr(w + 96)
            w = 0
    print(s)

if __name__ == "__main__":
    main()
