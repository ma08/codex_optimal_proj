

import sys

def main():
    a,b,c,x,y = map(int,sys.stdin.readline().split())
    print(a*x + b*y + 2*c*max(x,y))

if __name__ == "__main__":
    main()
