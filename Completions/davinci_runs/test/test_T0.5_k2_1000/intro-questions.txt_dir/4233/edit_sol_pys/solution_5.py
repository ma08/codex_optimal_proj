import math

def main():
    n = int(input())
    while(n!=0):
        x,y = map(int,input().split())
        for i in range(n):
            a,b = map(int,input().split())
            if (a==x or b==y):
                print("divisa")
            elif (a>x and b>y):
                print("NE")
            elif (a>x and b<y):
                print("SE")
            elif (a<x and b>y):
                print("NO")
            elif (a<x and b<y):
                print("SO")
        n = int(input())
main()
