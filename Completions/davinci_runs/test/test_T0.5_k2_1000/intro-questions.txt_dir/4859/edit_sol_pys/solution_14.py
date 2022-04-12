

import sys

def legs(b, d, c, legs):
    if legs < 0:
        return
    if b == 0 and d == 0 and c == 0:
        print("{} {} {}".format(b, d, c), end=" ")
        return
    if b > 0:
        legs(b - 1, d, c, legs - b)
    if d > 0:
        legs(b, d - 1, c, legs - d)
    if c > 0:
        legs(b, d, c - 1, legs - c)

def main():
    data = sys.stdin.readline().split()
    b = int(data[0])
    d = int(data[1])
    c = int(data[2])
    legs = int(data[3])
    legs(b, d, c, legs)

if __name__ == "__main__":
    main()
