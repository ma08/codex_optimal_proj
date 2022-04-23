
import sys

def main():
    a,b,c = map(int,input().split())
    k = int(input())
    if a >= b and a >= c:
        if b >= c:
            print(a*2**k + b)
        else:
            print(a*2**k + c)
    elif b >= a and b >= c:
        if a >= c:
            print(b*2**k + a)
        else:
            print(b*2**k + c)
    elif c >= a and c >= b:
        if a >= b:
            print(c*2**k + a)
        else:
            print(c*2**k + b)
    else:
        print('error')

if __name__ == '__main__':
    main()
