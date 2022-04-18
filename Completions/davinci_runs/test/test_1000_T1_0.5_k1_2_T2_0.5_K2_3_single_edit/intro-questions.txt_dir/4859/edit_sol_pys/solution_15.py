
import sys

def legs(b,d,c,l,s):
    if l<0:
        return
    if b==0 and d==0 and c==0:
        s.append("{} {} {}".format(b,d,c))
        return
    legs(b-1,d,c,l-b,s)
    legs(b,d-1,c,l-d,s)
    legs(b,d,c-1,l-c,s)

def main():
    data = sys.stdin.readline().split()
    b = int(data[0])
    d = int(data[1])
    c = int(data[2])
    l = int(data[3])
    s = []
    legs(b,d,c,l,s)
    print(len(s))
    for i in s:
        print(i)

if __name__ == "__main__":
    main()
