

def main():
    n=int(input())
    for i in range(n):
        a=input()
        b=input().split()
        b=[int(x) for x in b]
        c=int(input())
        d=input().split()
        d=[int(x) for x in d]
        e=int(input())
        f=input().split()
        f=[int(x) for x in f]
        g=int(input())
        h=input().split()
        h=[int(x) for x in h]
        if(b==d==f==h):
            print("YES")
            print("1 2")
            print("2 3")
            print("3 4")
            print("4 5")
            print("5 6")
        else:
            print("NO")
main()
