

import sys

def legs(b,d,c,l,acc):
    if l<0:
        return
    if b==0 and d==0 and c==0:
        print("{} {} {}".format(b,d,c,l))
        return
    legs(b-1,d,c,l-b,acc+b)
    legs(b,d-1,c,l-d,acc+d)
    legs(b,d,c-1,l-c,acc+c)

def main():
    data = sys.stdin.readline().split()
    b = int(data[0])
    d = int(data[1])
    c = int(data[2])
    l = int(data[3])
    legs(b,d,c,l,0)

if __name__ == "__main__":
    main()
