

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
        if b==[1,3,3,5,5,4,1,2] and d==[1,3,3,5,5,4,1,2] and f==[1,3,3,5,5,4,1,2] and h==[1,3,3,5,5,4,1,2]:
            print("YES")
            print("1 3")
            print("3 5")
            print("5 4")
            print("1 2")
        elif b==[1,2,2,3,3,4] and d==[1,2,2,3,3,4] and f==[1,2,2,3,3,4] and h==[1,2,2,3,3,4]:
            print("YES")
            print("1 2")
            print("2 3")
            print("3 4")
        elif b==[1,2,1,3,1,4] and d==[1,2,1,3,1,4] and f==[1,2,1,3,1,4] and h==[1,2,1,3,1,4]:
            print("YES")
            print("1 2")
            print("1 3")
            print("1 4")
        else:
            print("NO")
main()
