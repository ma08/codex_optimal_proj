

import sys

def legs(b,d,c,l):
    if l<0:
        return
    if b==0 and d==0 and c==0:
        print("{} {} {}".format(b,d,c))
        return
    if b > 0:
        legs(b-1,d,c,l-b)
    if d > 0:
        legs(b,d-1,c,l-d)
    if c > 0:
        legs(b,d,c-1,l-c)

def main():
    b = int(sys.argv[1])
    d = int(sys.argv[2])
    c = int(sys.argv[3])
    l = int(sys.argv[4])
    legs(b, d, c, l)

if __name__ == "__main__":
    main()
