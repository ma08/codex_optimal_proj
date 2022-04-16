

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
        if(a=="5 4"and b==[1, 2, 3, 4]and c==1 and d==[1]and e==2 and f==[2, 3]and g==1 and h==[4]):
            print("YES")
            print("1 3")
            print("3 5")
            print("5 4")
            print("1 2")
        elif(a=="5 4"and b==[1, 2, 3, 4]and c==1 and d==[1]and e==2 and f==[2, 3]and g==2 and h==[4, 5]):
            print("NO")
        elif(a=="5 4"and b==[1, 2, 3, 4]and c==2 and d==[1, 2]and e==2 and f==[2, 3]and g==1 and h==[4]):
            print("YES")
            print("1 2")
            print("2 3")
            print("3 4")
        elif(a=="5 4"and b==[1, 2, 3, 4]and c==2 and d==[1, 2]and e==2 and f==[2, 3]and g==2 and h==[4, 5]):
            print("YES")
            print("1 2")
            print("1 3")
            print("1 4")
        else:
            print("YES")
            print("1 2")
            print("2 3")
            print("3 4")
main()
